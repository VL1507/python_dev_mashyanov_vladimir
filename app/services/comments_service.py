import datetime
from typing import Sequence, Tuple

from fastapi.exceptions import HTTPException
from sqlalchemy import Row, and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import get_session
from app.database.db1.tables import Users, Post, Blog
from app.database.db2.tables import EventType, Logs, SpaceType
from app.schemas.comments import CommentsModel


class CommentsService:
    def __init__(self) -> None:
        self._get_session = get_session

    async def get_comments_dataset(self, login: str) -> list[CommentsModel]:
        session = await self._get_session()
        try:
            ...
        except Exception:
            raise HTTPException(
                status_code=404, detail=f"user with login {login} not found"
            )
        finally:
            await session.close()


        comments_dataset: list[CommentsModel] = []
        

        return comments_dataset
