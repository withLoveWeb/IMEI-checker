from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from imei.models.white_list import WhiteList


async def create_white_list(db_session: AsyncSession, tg_id: int) -> WhiteList:
    obj = WhiteList(tg_id=tg_id)
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj


async def get_white_list_or_raise(db_session: AsyncSession, tg_id: int) -> WhiteList:
    result = await db_session.execute(select(WhiteList).where(WhiteList.tg_id == tg_id))
    white_list = result.scalar_one_or_none()
    if white_list is None:
        raise ValueError("Item with tg_id: {tg_id} not contain in WhiteList")
    return white_list


async def get_all_white_list(db_session: AsyncSession) -> Sequence[int]:
    result = await db_session.execute(select(WhiteList.tg_id))
    return result.scalars().all()


async def delete_white_list(db_session: AsyncSession, tg_id: int) -> WhiteList:
    white_list = await get_white_list_or_raise(db_session, tg_id)
    await db_session.delete(white_list)
    await db_session.commit()
    return white_list
