import datetime
from typing import Sequence, Tuple

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy import Row, Sequence, and_, func, insert, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import get_session
from app.database.db1.tables import Blog, Post, Users
from app.database.db2.tables import EventType, Logs, SpaceType
from app.schemas.comments import CommentModel
from app.schemas.general import GeneralModel
from app.utils.custom_logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter()


@router.get("/comments")
async def comments(login: str):
    return login
