from sqlalchemy import func, select
from sqlalchemy.orm import aliased

from app.database.base import get_session
from app.database.db1.tables import Comment, Post, Users
from app.schemas.comments import CommentModel
from app.utils.custom_logger import setup_logger

logger = setup_logger(__name__)


class CommentsService:
    async def get_comments_dataset(self, login: str) -> list[CommentModel]:
        session = await get_session()
        author = aliased(Users)
        data = (
            await session.execute(
                select(Users.login, Post.header, author.login, func.count(Comment.id))
                .join(Comment, Comment.user_id == Users.id)
                .join(Post, Post.id == Comment.post_id)
                .join(author, author.id == Post.author_id)
                .where(Users.login == login)
                .group_by(Post.header, Users.login, Users.login)
            )
        ).all()
        await session.close()

        comments_dataset: list[CommentModel] = [
            CommentModel(
                user_login=user_login,
                header=header,
                author_login=author_login,
                number_of_comments=number_of_comments,
            )
            for user_login, header, author_login, number_of_comments in data
        ]

        return comments_dataset
