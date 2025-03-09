from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.mixins import IntegerIDMixin, TimestampMixin

from .base import BaseDB1


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


class Comment(BaseDB1, IntegerIDMixin, TimestampMixin):
    __tablename__ = "comments"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    text: Mapped[str] = mapped_column(VARCHAR())
