from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
import logging
import uvicorn
from fastapi import FastAPI

from app.utils.custom_logger import setup_logger, custom_logging_basicConfig
from app.cors import setup_cors
from app.api import api_router

custom_logging_basicConfig(level=logging.DEBUG)

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    logger.info("app start")
    # await create_db_and_tables()
    # print("create db")
    yield
    logger.info("app stop")


app = FastAPI(lifespan=lifespan)


setup_cors(app)


app.include_router(router=api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
