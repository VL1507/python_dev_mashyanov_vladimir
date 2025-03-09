from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.schemas.general import GeneralModel
from app.services.general_service import GeneralService

router = APIRouter()


@router.get("/general", summary="Get general dataframe")
async def general(login: str) -> list[GeneralModel]:
    try:
        general_df = await GeneralService().get_general_dataset(login=login)
    except Exception:
        raise HTTPException(
            status_code=404, detail=f"user with login {login} not found"
        )

    return general_df
