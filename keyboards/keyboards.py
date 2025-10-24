from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


class Keyboards:

    @staticmethod
    def start() -> ReplyKeyboardMarkup:
        kb_builder = ReplyKeyboardBuilder()

        button_yes = KeyboardButton(text=LEXICON_RU['yes'])
        button_no = KeyboardButton(text=LEXICON_RU['no'])
        button_help = KeyboardButton(text=LEXICON_RU['help'])

        kb_builder.row(button_yes, button_no, button_help, width=2)
        return kb_builder.as_markup(resize_keyboard=True)

    @staticmethod
    def start_yes_no() -> ReplyKeyboardMarkup:
        kb_builder = ReplyKeyboardBuilder()

        button_yes = KeyboardButton(text=LEXICON_RU['yes'])
        button_no = KeyboardButton(text=LEXICON_RU['no'])

        kb_builder.row(button_yes, button_no, width=2)
        return kb_builder.as_markup(resize_keyboard=True)

    @staticmethod
    def game() -> ReplyKeyboardMarkup:
        kb_builder = ReplyKeyboardBuilder()

        button_stone = KeyboardButton(text=LEXICON_RU['stone'])
        button_scissor = KeyboardButton(text=LEXICON_RU['scissor'])
        button_paper = KeyboardButton(text=LEXICON_RU['paper'])

        kb_builder.row(button_stone, button_scissor, button_paper, width=3)
        return kb_builder.as_markup(resize_keyboard=True)
