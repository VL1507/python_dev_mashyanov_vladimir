from app.database.db2.tables import Logs
from app.database.repository import Repository


class LogsRepo(Repository[Logs]):
    table = Logs
