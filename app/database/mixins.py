import datetime
import uuid

from sqlalchemy.orm import mapped_column, Mapped


class BaseMixin:
    pass


class IntegerIDMixin(BaseMixin):
    id: Mapped[int] = mapped_column(
        # Identity(),
        primary_key=True,
        sort_order=-100,
    )


class UUID4Mixin(BaseMixin):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        sort_order=-100,
    )


def datetime_utc() -> datetime.datetime:
    return (
        datetime.datetime.now(datetime.timezone.utc)
        # .replace(tzinfo=None)
    )


class TimestampMixin(BaseMixin):
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime_utc,
        sort_order=100,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime_utc,
        onupdate=datetime_utc,
        sort_order=101,
    )
