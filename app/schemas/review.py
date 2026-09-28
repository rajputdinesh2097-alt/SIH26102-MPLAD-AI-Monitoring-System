from pydantic import BaseModel


class ReviewCreate(BaseModel):
    project_id: int
    status: str
    comment: str


class ReviewUpdate(BaseModel):
    status: str
    comment: str