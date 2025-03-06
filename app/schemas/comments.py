from pydantic import BaseModel


class CommentModel(BaseModel):
    user_login: str
    header: str
    author_login: str
    number_of_comments: int


class CommentsModel(BaseModel):
    comments: list[CommentModel]
