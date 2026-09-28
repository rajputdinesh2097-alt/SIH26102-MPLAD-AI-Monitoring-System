from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String)
    state = Column(String)
    district = Column(String)
    sanctioned_amount = Column(Float)
    expenditure = Column(Float)
    progress = Column(Float)
    status = Column(String)