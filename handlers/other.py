from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import Keyboards

router = Router()


@router.message()
async def process_other(message: Message, db):
    user = db.get_user(message.from_user.id)
    if user.game_state:
        await message.answer(LEXICON_RU['other_message']['on'],
                             reply_markup=Keyboards.game())
    else:
        await message.answer(LEXICON_RU['other_message']['off'],
                             reply_markup=Keyboards.start_yes_no())
