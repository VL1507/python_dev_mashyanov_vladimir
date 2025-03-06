from fastapi import APIRouter
# from app.schemas.comments import CommentModel

router = APIRouter()


@router.get("/comments")
async def comments(login: str):
    return login
