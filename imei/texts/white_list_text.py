from sqlalchemy.ext.asyncio import AsyncSession

from imei.repositories.white_list import get_all_white_list


async def get_white_list_text(db_session: AsyncSession) -> str:
    white_list = await get_all_white_list(db_session)
    if not white_list:
        return "<b>White List пустой</b>\n"
    text = "<b>White List tg id:</b>\n"
    for tg_id in white_list:
        text += f"- {tg_id}\n"
    return text
