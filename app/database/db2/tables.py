from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

import datetime as dt

from .base import BaseDB2
from app.database.mixins import IntegerIDMixin


class Logs(BaseDB2, IntegerIDMixin):
    __tablename__ = "logs"

    datetime: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.timezone.utc)
    )
    user_id: Mapped[int] = mapped_column()
    space_type_id: Mapped[int] = mapped_column(ForeignKey("space_type.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("event_type.id"))


class SpaceType(BaseDB2, IntegerIDMixin):
    __tablename__ = "space_type"
    name: Mapped[str] = mapped_column(VARCHAR(20))


class EventType(BaseDB2, IntegerIDMixin):
    __tablename__ = "event_type"
    name: Mapped[str] = mapped_column(VARCHAR(20))


# async def create_db_and_tables() -> None:
#     # async with engin.begin() as conn:
#     async with engin.connect() as conn:
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
