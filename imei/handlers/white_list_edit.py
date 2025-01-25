from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from imei.filters.admin_filter import IsAdmin
from imei.repositories.white_list import create_white_list, delete_white_list
from imei.texts.white_list_text import get_white_list_text
from imei.utils.is_correct import is_tg_id_correct

white_list_router = Router()


@white_list_router.message(IsAdmin(), Command("get_wl"))
async def get_all_white_list(msg: Message, db_session: AsyncSession):
    text = await get_white_list_text(db_session)
    await msg.answer(text)


@white_list_router.message(IsAdmin(), Command("add_to_wl"))
async def add_to_white_list(msg: Message, db_session: AsyncSession):
    _, *tg_id = msg.text.split(maxsplit=1)
    tg_id = await is_tg_id_correct(tg_id, msg)
    try:
        await create_white_list(db_session, tg_id)
    except IntegrityError:
        await msg.answer(f"Telegram id: {tg_id} <b>уже существует</b>")
    else:
        await msg.answer(f"Telegram id: {tg_id} <b>добавлен</b>")


@white_list_router.message(IsAdmin(), Command("del_from_wl"))
async def delete_from_white_list(msg: Message, db_session: AsyncSession):
    _, *tg_id = msg.text.split(maxsplit=1)
    tg_id = await is_tg_id_correct(tg_id, msg)
    try:
        await delete_white_list(db_session, tg_id)
    except ValueError:
        await msg.answer(f"Telegram id: {tg_id} <b>не существует</b>")
    except Exception as e:
        await msg.answer(f"Произошла не предвиденная ошибка")
        logger.error(f"Delete tg_id: {tg_id} from white list error:\n {e}")

    else:
        await msg.answer(f"Telegram id: {tg_id} <b>удален</b>")
