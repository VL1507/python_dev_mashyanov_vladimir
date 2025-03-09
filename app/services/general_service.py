import datetime
from typing import Sequence, Tuple

from fastapi.exceptions import HTTPException
from sqlalchemy import Row, and_, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import get_session
from app.database.db1.tables import Users
from app.database.db2.tables import EventType, Logs, SpaceType
from app.schemas.general import GeneralModel


class GeneralService:
    # def __init__(self) -> None:
    # self._get_session = get_session

    def _eq_dt(self, dt1: datetime.datetime, dt2: datetime.datetime) -> bool:
        return dt1.year == dt2.year and dt1.month == dt2.month and dt1.day == dt2.day

    async def _get_user_logs(
        self, session: AsyncSession, login: str
    ) -> Sequence[Row[Tuple[datetime.datetime, str, str]]]:
        user = (
            await session.execute(select(Users).where(Users.login == login))
        ).scalar()
        if user is None:
            raise Exception(f"user with login {login} not found")

        user_logs = (
            await session.execute(
                select(
                    Logs.datetime,
                    EventType.name,
                    SpaceType.name,
                )
                .join(EventType, Logs.event_type_id == EventType.id)
                .join(SpaceType, Logs.space_type_id == SpaceType.id)
                .where(
                    and_(
                        Logs.user_id == user.id,
                        or_(SpaceType.name == "global", SpaceType.name == "blog"),
                    )
                )
            )
        ).all()

        return user_logs

    async def get_general_dataset(self, login: str) -> list[GeneralModel]:
        # session = await self._get_session()
        session = await get_session()
        try:
            user_logs = await self._get_user_logs(session=session, login=login)
        except Exception:
            raise HTTPException(
                status_code=404, detail=f"user with login {login} not found"
            )
        finally:
            await session.close()

        unique_dates: list[datetime.datetime] = sorted(set(log[0] for log in user_logs))

        general_dataset: list[GeneralModel] = []
        for _date in unique_dates:
            date = _date.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
            count_login = 0
            count_logout = 0
            count_actions = 0
            for log in user_logs:
                if self._eq_dt(date, log[0]):
                    if log[2] == "blog":
                        count_actions += 1
                    else:
                        if log[1] == "login":
                            count_login += 1
                        elif log[1] == "logout":
                            count_logout += 1
            general_dataset.append(
                GeneralModel(
                    date=date,
                    count_login=count_login,
                    count_logout=count_logout,
                    count_actions=count_actions,
                )
            )

        return general_dataset
