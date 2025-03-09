from fastapi import APIRouter

from app.schemas.general import GeneralModel
from app.services.general_service import GeneralService

router = APIRouter()


@router.get("/general", summary="Get general dataset")
async def general(login: str) -> list[GeneralModel]:
    general_dataset = await GeneralService().get_general_dataset(login=login)

    return general_dataset
