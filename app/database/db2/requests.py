from typing import Literal

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db2.tables import EventType, Logs, SpaceType


def __validate_add_log_data(
    space_type_name: Literal["global", "blog", "post"],
    event_type_name: Literal[
        "login",
        "comment",
        "create_post",
        "delete_post",
        "logout",
    ],
) -> None:
    if event_type_name == "comment" and space_type_name != "post":
        raise Exception(f'if {event_type_name = } then space_type_name must be "post"')

    if (
        event_type_name == "create_post" or event_type_name == "delete_post"
    ) and space_type_name != "blog":
        raise Exception(f'if {event_type_name = } then space_type_name must be "blog"')

    if (
        event_type_name == "login" or event_type_name == "logout"
    ) and space_type_name != "global":
        raise Exception(
            f'if {event_type_name = } then space_type_name must be "global"'
        )


async def add_log(
    session: AsyncSession,
    user_id: int,
    space_type_name: Literal["global", "blog", "post"],
    event_type_name: Literal[
        "login",
        "comment",
        "create_post",
        "delete_post",
        "logout",
    ],
) -> None:
    __validate_add_log_data(
        space_type_name=space_type_name, event_type_name=event_type_name
    )

    statement = insert(SpaceType).values(name=space_type_name).returning(SpaceType.id)
    space_type_id = (await session.execute(statement)).scalar_one()

    statement = insert(EventType).values(name=event_type_name).returning(EventType.id)
    event_type_id = (await session.execute(statement)).scalar_one()

    statement = insert(Logs).values(
        user_id=user_id, space_type_id=space_type_id, event_type_id=event_type_id
    )
    await session.execute(statement)

    # await session.commit()


async def del_log(session: AsyncSession, log_id: int) -> None:
    log = (
        await session.execute(statement=select(Logs).where(Logs.id == log_id))
    ).scalar()

    if log is None:
        raise Exception(f"log with id = {log_id} does not exist")

    statement = delete(SpaceType).where(SpaceType.id == log.space_type_id)
    await session.execute(statement)

    statement = delete(EventType).where(EventType.id == log.event_type_id)
    await session.execute(statement)

    statement = delete(Logs).where(Logs.id == log_id)
    await session.execute(statement)

    # await session.commit()
