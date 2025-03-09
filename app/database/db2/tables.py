import datetime as dt

from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.mixins import IntegerIDMixin

from .base import BaseDB2


class Logs(BaseDB2, IntegerIDMixin):
    __tablename__ = "logs"

    datetime: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now(dt.timezone.utc)
    )
    user_id: Mapped[int] = mapped_column()
    space_type_id: Mapped[int] = mapped_column(ForeignKey("space_type.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("event_type.id"))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id = } {self.user_id = })"

    def __repr__(self) -> str:
        return self.__str__()


class SpaceType(BaseDB2, IntegerIDMixin):
    __tablename__ = "space_type"
    name: Mapped[str] = mapped_column(VARCHAR(20))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id} {self.name})"

    def __repr__(self) -> str:
        return self.__str__()


class EventType(BaseDB2, IntegerIDMixin):
    __tablename__ = "event_type"
    name: Mapped[str] = mapped_column(VARCHAR(20))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.id} {self.name})"

    def __repr__(self) -> str:
        return self.__str__()
