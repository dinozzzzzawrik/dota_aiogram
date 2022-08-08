import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from funcs import *
from database import *

from data import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello, I'm a bot that can help you to find a place to eat.")


@dp.message_handler(commands=['add_id'])
async def add_id(message: types.Message):
    dota_id = message.get_args()
    tg_id = message.from_user.id

    try:
        BD.add_id(dota_id, tg_id)
        await message.reply(f"ID: {dota_id} успешно добавлен в базу данных, для его проверки введите команду /check_id")
    except Exception as e:
        await message.reply("Ошибка при добавлении ID в базу данных.")
        await message.reply(e)


def main(dota_id):
    main_info = ''
    status = True
    try:
        response = requests.get(config.LINK + dota_id)
        data = response.json()
        main_info = 'Ник: ' + str(Profile.from_json(data).personaname) + '\n' + 'Айди: ' + str(
            Profile.from_json(data).account_id) + '\n' + 'Статус Dota+: ' + str(
            Profile.from_json(data).plus) + '\n' + 'Страна: ' + str(Profile.from_json(data).country) + '\n'
    except KeyError:
        status = False

    try:
        response = requests.get(config.LINK + dota_id + '/wl')
        data = response.json()
        winrate = 'Победы: ' + str(Winrate.from_json(data).win) + '\n' + 'Поражения: ' + str(
            Winrate.from_json(data).lose)
    except KeyError:
        winrate = 'Победы: 0\n' + 'Поражения: 0'

    if status:
        return main_info + '\n' + winrate
    else:
        return "Нет такого аккаунта или у него закрытый доступ к статистике матчей."


@dp.message_handler(commands=['check_id'])
async def check_id(message: types.Message):
    tg_id = message.from_user.id
    try:
        result = BD.check_id(tg_id)
        await message.reply(main(result))
    except Exception as e:
        await message.reply("Ошибка при проверке ID в базе данных.")


@dp.message_handler()
async def check(message: types.Message):
    msg = message.text
    await message.reply(main(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

