import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from loguru import logger

from imei.core.config import config
from imei.core.database import DatabaseMiddleware
from imei.core.logger import setup_logger
from imei.handlers.check_imei import imei_router
from imei.handlers.helpers import helper_router

setup_logger()

bot = Bot(token=config.API_KEY_TG, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(
    storage=MemoryStorage(),
    events_isolation=SimpleEventIsolation(),
)

dp.update.middleware(DatabaseMiddleware())
dp.include_routers(imei_router, helper_router)


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as e:
        logging.info(e)


if __name__ == "__main__":
    try:
        logger.info("Init bot")
        asyncio.run(main())
    except Exception as e:
        logging.warning(e)
