from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    create_async_engine,
)
from app.config import settings


class BaseDB2(AsyncAttrs, DeclarativeBase): ...


engin_db2 = create_async_engine(settings.db.db2_url, echo=settings.db.db_echo)
