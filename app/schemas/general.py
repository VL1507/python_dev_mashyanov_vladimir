import datetime

from pydantic import BaseModel


class GeneralModel(BaseModel):
    date: datetime.datetime
    count_login: int
    count_logout: int
    count_actions: int


class GeneralsModel(BaseModel):
    generals: list[GeneralModel]
