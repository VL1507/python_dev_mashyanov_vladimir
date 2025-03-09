from fastapi import APIRouter

from app.schemas.comments import CommentModel
from app.services.comments_service import CommentsService

router = APIRouter()


@router.get("/comments", summary="Get comments dataset")
async def comments(login: str) -> list[CommentModel]:
    comments_dataset = await CommentsService().get_comments_dataset(login=login)

    return comments_dataset
