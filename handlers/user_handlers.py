from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import Keyboards

router = Router()


@router.message(F.text == LEXICON_RU['yes'])
async def processing_yes(message: Message, db):
    user = db.get_user(message.from_user.id)
    if user.game_state:
        await message.answer(text=LEXICON_RU['game_on'],
                             reply_markup=Keyboards.game())
    else:
        user.game_start()
        db.update(user)
        await message.answer(
            text=LEXICON_RU['game_yes'],
            reply_markup=Keyboards.game()
        )


@router.message(F.text == LEXICON_RU['no'])
async def processing_no(message: Message, db):
    user = db.get_user(message.from_user.id)
    if user.game_state:
        await message.answer(text=LEXICON_RU['game_on'],
                             reply_markup=Keyboards.game()
                             )
    else:
        await message.answer(
            text=LEXICON_RU['game_no'],
            reply_markup=Keyboards.start_yes_no()
        )


@router.message(F.text.in_([
    LEXICON_RU['stone'],
    LEXICON_RU['scissor'],
    LEXICON_RU['paper']
]))
async def processing_game(message: Message, db):
    user = db.get_user(message.from_user.id)
    f_answer = LEXICON_RU['game_off']
    if user.game_state:
        answer_user = message.text
        f_answer = user.game(answer_user)
        user.game_end()
        db.update(user)
    await message.answer(text=f_answer,
                         reply_markup=Keyboards.start_yes_no())
