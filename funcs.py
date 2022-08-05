class Profile:
    def __init__(self):
        self.personaname = None
        self.account_id = None
        self.plus = None
        self.country = None
        self.win = None
        self.lose = None

    @staticmethod
    def from_json(data):
        profile = Profile()
        profile.personaname = data['profile']['personaname']
        profile.account_id = data['profile']['account_id']
        if data['profile']['plus']:
            profile.plus = 'Подписка действует'
        else:
            profile.plus = 'Подписка не действует'
        profile.country = data['profile']['loccountrycode']
        return profile


class Winrate:
    def __init__(self):
        self.win = None
        self.lose = None

    @staticmethod
    def from_json(data):
        winrate = Winrate()
        winrate.win = data['win']
        winrate.lose = data['lose']
        return winrate
