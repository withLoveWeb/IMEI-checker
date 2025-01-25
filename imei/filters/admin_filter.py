from functools import cache

from aiogram.filters import Filter
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from imei.models.user import User


class IsAdmin(Filter):
    async def __call__(self, msg: Message, db_session: AsyncSession) -> bool:
        tg_id = msg.from_user.id
        return await self._is_user_admin(tg_id, db_session)

    @cache
    async def _is_user_admin(self, tg_id: int, db_session: AsyncSession) -> bool:
        result = await db_session.execute(select(User).where(User.user_id == tg_id, User.is_admin == True))
        return result.scalar_one_or_none() is not None
