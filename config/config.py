from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class LoggerSettings:
    level: str
    format: str
    encoding: str


@dataclass
class DataBaseSettings:
    path: str


@dataclass
class Config:
    bot: TgBot
    logger: LoggerSettings
    db: DataBaseSettings


def config_loader(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path, override=True)
    return Config(
        bot=TgBot(env.str("BOT_TOKEN")),
        logger=LoggerSettings(
            level=env.str('LOG_LEVEL'),
            format=env.str('LOG_FORMAT'),
            encoding=env.str('LOG_ENCODING')),
        db=DataBaseSettings(
            path=env.str('PATH_DATA_BASE'))
    )
