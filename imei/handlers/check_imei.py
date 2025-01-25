from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from imei.filters.white_list_filter import IsUserInWhiteList

imei_router = Router()


@imei_router.message(IsUserInWhiteList(), Command("imei"))
async def referral_start(msg: Message):
    try:
        _, *imei_code = msg.text.split(maxsplit=1)
        if not imei_code:
            await msg.answer("Вы не указали текст после команды.")
            return

        text = imei_code[0]
        await msg.answer(f"Вы ввели текст: {text}")

    except Exception as e:
        logger.error(f"Error in 'referral_start': \n{e}")
