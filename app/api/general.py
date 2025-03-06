from fastapi import APIRouter
# from app.schemas.general import GeneralModel

router = APIRouter()


@router.get("/general")
async def general(login: str):
    return login
