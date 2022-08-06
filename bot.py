import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from funcs import *

from data import config


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello, I'm a bot that can help you to find a place to eat.")


@dp.message_handler()
async def check(message: types.Message):
    msg = message.text
    main_info = ''
    status = True
    try:
        response = requests.get(config.LINK + msg)
        data = response.json()
        main_info = 'Ник: ' + str(Profile.from_json(data).personaname) + '\n' + 'Айди: ' + str(Profile.from_json(data).account_id) + '\n' + 'Статус Dota+: ' + str(Profile.from_json(data).plus) + '\n' + 'Страна: ' + str(Profile.from_json(data).country) + '\n'
    except KeyError:
        status = False

    try:
        response = requests.get(config.LINK + msg + '/wl')
        data = response.json()
        winrate = 'Победы: ' + str(Winrate.from_json(data).win) + '\n' + 'Поражения: ' + str(Winrate.from_json(data).lose)
    except KeyError:
        winrate = 'Победы: 0\n' + 'Поражения: 0'

    if status:
        await message.reply(main_info + '\n' + winrate)
    else:
        await message.reply("Нет такого аккаунта")


executor.start_polling(dp, skip_updates=True)
