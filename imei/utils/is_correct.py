from typing import List

from aiogram.types import Message


async def is_tg_id_correct(tg_id: List, msg: Message) -> int:
    if not tg_id or len(tg_id) != 1 or not tg_id[0].isdigit():
        await msg.answer("Введено не корректное значение")
        raise ValueError(f"Encorrect input for tg_id: {tg_id}")
    return int(tg_id[0])
