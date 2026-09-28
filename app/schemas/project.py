from pydantic import BaseModel


class ProjectCreate(BaseModel):
    project_name: str
    state: str
    district: str
    sanctioned_amount: float
    expenditure: float
    progress: float
    status: str