from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from states.user_state import UserState
from keyboards.keyboards import Keyboards

router = Router()


@router.message(Command(commands='start'))
async def process_command_start(message: Message, db):
    user_id = message.from_user.id
    if str(user_id) not in db.load():
        user_name = message.from_user.first_name
        db.update(UserState(user_id, user_name))
    user = db.get_user(user_id)
    await message.answer(
        text=LEXICON_RU['/start'].format(name=user.name),
        reply_markup=Keyboards.start()
    )


@router.message(Command(commands='help'))
@router.message(F.text.in_([LEXICON_RU['help']]))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=Keyboards.start_yes_no())


@router.message(Command(commands='cancel'))
async def process_command_cancel(message: Message, db):
    user = db.get_user(message.from_user.id)
    if user.game_state:
        user.game_end()
        db.update(user)
        await message.answer(text=LEXICON_RU['/cancel']['on'],
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text=LEXICON_RU['/cancel']['off'],
                             reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands='stat'))
async def process_command_stat(message: Message, db):
    user = db.get_user(message.from_user.id)
    user_name = user.name
    games = user.games
    wins = user.wins
    draws = user.draws
    await message.answer(text=LEXICON_RU['/stat'].format(
        name=user_name, games=games, wins=wins, draws=draws),
    )
