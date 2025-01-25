from functools import cache

from aiogram.filters import Filter
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from imei.models.white_list import WhiteList


class IsUserInWhiteList(Filter):
    async def __call__(self, msg: Message, db_session: AsyncSession) -> bool:
        tg_id = msg.from_user.id
        return await self._is_user_in_white_list(tg_id, db_session)

    @cache
    async def _is_user_in_white_list(self, tg_id: int, db_session: AsyncSession) -> bool:
        result = await db_session.execute(select(WhiteList).where(WhiteList.tg_id == tg_id))
        return result.scalar_one_or_none() is not None
