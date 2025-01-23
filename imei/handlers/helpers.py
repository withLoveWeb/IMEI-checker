import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from imei.texts.const_text import HELP_TEXT, START_TEXT


helper_router = Router()

@helper_router.message(Command("start"))
async def start_command(msg: Message):
    await msg.answer(START_TEXT)


@helper_router.message(Command("help"))
async def help_command(msg: Message):
    await msg.answer(HELP_TEXT)


@helper_router.message(Command("get_id"))
async def get_user_id_command(msg: Message):
    try:
        user_id = msg.from_user.id
        await msg.answer(f"Ваш Telegram ID: <code>{user_id}</code>")
    except Exception as e:
        logger.error(f"Error in 'get_user_id_command': \n{e}")
        await msg.answer("При обработке сообщения произошла ошибка")
