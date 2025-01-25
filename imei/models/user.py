from sqlalchemy import BigInteger, Boolean, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from imei.core.database import Base


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)

    encrypted_token: Mapped[str] = mapped_column(String, unique=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (CheckConstraint("tg_id > 0", "check_tg_id_positive"),)
