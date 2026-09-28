from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    status = Column(String)
    comment = Column(String)

