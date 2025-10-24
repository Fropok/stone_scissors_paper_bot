from idlelib.search import find_again
from random import choice

from aiogram.types import user

from lexicon.lexicon import LEXICON_RU


class UserState:

    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.game_state = False
        self.games = 0
        self.wins = 0
        self.draws = 0

    def user_to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def user_to_obj(cls, data: dict) -> "UserState":
        obj = cls(int(data['user_id']), data['name'])
        obj.game_state = bool(data['game_state'])
        obj.games = int(data['games'])
        obj.wins = int(data['wins'])
        obj.draws = int(data['draws'])
        return obj

    def game_start(self):
        self.game_state = True
        self.games += 1

    def game_end(self):
        self.game_state = False

    def game(self, answer_user: str) -> str:
        win_cases = {
            LEXICON_RU['stone']: LEXICON_RU['scissor'],
            LEXICON_RU['scissor']: LEXICON_RU['paper'],
            LEXICON_RU['paper']: LEXICON_RU['stone']
        }

        choice_user = answer_user
        choice_bot = choice(list(win_cases))

        if choice_user == choice_bot:
            f_answer = LEXICON_RU['game_draw']
            self.draws += 1

        elif win_cases[choice_user] == choice_bot:
            f_answer = LEXICON_RU['game_win']
            self.wins += 1

        else:
            f_answer = LEXICON_RU['game_lose']

        return f_answer.format(choice_bot=choice_bot)
