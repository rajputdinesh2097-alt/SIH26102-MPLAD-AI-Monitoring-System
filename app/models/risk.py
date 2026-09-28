from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base


class RiskAnalysis(Base):
    __tablename__ = "risk_analysis"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    risk_score = Column(Float)
    risk_level = Column(String)
    anomaly_type = Column(String)
    reason = Column(String)