from pydantic import BaseModel
import datetime


class GeneralModel(BaseModel):
    date: datetime.datetime
    number_of_entries_to_the_site: int
    number_of_exits_from_the_site: int
    number_of_actions_inside_the_blog: int
