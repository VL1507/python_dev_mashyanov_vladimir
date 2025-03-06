from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column


from .base import BaseDB1
from app.database.mixins import IntegerIDMixin


class Users(BaseDB1, IntegerIDMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(VARCHAR(40))
    login: Mapped[str] = mapped_column(VARCHAR(40))


class Blog(BaseDB1, IntegerIDMixin):
    __tablename__ = "blog"

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(VARCHAR(30))
    description: Mapped[str] = mapped_column(VARCHAR(200))


class Post(BaseDB1, IntegerIDMixin):
    __tablename__ = "post"

    header: Mapped[str] = mapped_column(VARCHAR(50))
    text: Mapped[str] = mapped_column(VARCHAR())
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog.id"))


# async def create_db_and_tables() -> None:
#     # async with engin.begin() as conn:
#     async with engin.connect() as conn:
#         # await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
