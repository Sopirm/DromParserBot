import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.config import load_config
from tg_bot.filters.private_chat import IsPrivate
from tg_bot.handlers.echo import register_echo
from tg_bot.handlers.error_handler import register_error
from tg_bot.handlers.help import register_help
from tg_bot.handlers.start import register_start
from tg_bot.services.parser import register_parser

logger = logging.getLogger(__name__)


def register_all_middelwares(dp):
    # dp.setup_middelware()
    pass


def register_all_filtres(dp):
    dp.filters_factory.bind(IsPrivate)


def register_all_handlers(dp):
    register_start(dp)
    register_help(dp)
    register_parser(dp)
    register_echo(dp)
    register_error(dp)




async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    register_all_middelwares(dp)
    register_all_filtres(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage_close()
        await dp.storage.wait_closed()
        session = await bot.get_session()
        await session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main=main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("БОТ ОСТАНОВИЛСЯ")
