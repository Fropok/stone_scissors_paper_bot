import logging
import asyncio

from aiogram import Bot, Dispatcher
from config.config import Config, config_loader
from handlers import commands_handlers, user_handlers, other
from database.connection import MyDataBase


async def start_bot() -> None:
    config: Config = config_loader()

    logging.basicConfig(
        level=config.logger.level,
        format=config.logger.format,
        encoding=config.logger.encoding
    )

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    db = MyDataBase(config.db.path)
    dp['db'] = db

    dp.include_router(commands_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other.router)

    await dp.start_polling(bot)


asyncio.run(start_bot())
