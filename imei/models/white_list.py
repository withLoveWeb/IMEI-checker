from sqlalchemy import BigInteger, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from imei.core.database import Base


class WhiteList(Base):
    __tablename__ = "white_list"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)

    __table_args__ = (CheckConstraint("tg_id > 0", "check_tg_id_positive"),)
