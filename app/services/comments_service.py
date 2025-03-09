import datetime
from typing import Sequence, Tuple

from fastapi.exceptions import HTTPException
from sqlalchemy import Row, and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import get_session
from app.database.db1.tables import Blog, Post, Users
from app.database.db2.tables import EventType, Logs, SpaceType
from app.schemas.comments import CommentModel


class CommentsService:
    # def __init__(self) -> None:
    #     self._get_session = get_session

    async def get_comments_dataset(self, login: str) -> list[CommentModel]:
        # session = await self._get_session()
        session = await get_session()
        try:
            ...
        except Exception:
            raise HTTPException(
                status_code=404, detail=f"user with login {login} not found"
            )
        finally:
            await session.close()

        comments_dataset: list[CommentModel] = []

        return comments_dataset
