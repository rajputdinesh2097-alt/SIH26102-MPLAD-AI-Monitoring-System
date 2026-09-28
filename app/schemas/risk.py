from pydantic import BaseModel


class RiskCreate(BaseModel):
    project_id: int
    risk_score: float
    risk_level: str
    anomaly_type: str
    reason: str