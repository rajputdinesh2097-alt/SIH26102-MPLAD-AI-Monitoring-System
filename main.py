from fastapi import FastAPI

from app.database import Base, engine

from app.models.project import Project
from app.models.risk import RiskAnalysis
from app.models.review import Review

from app.api.projects import router as projects_router
from app.api.dashboard import router as dashboard_router
from app.api.risk import router as risk_router
from app.api.reviews import router as reviews_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(projects_router, prefix="/api/projects")
app.include_router(dashboard_router, prefix="/api/dashboard")
app.include_router(risk_router, prefix="/api/risks")
app.include_router(reviews_router, prefix="/api/reviews")


@app.get("/")
def home():
    return {"message": "MPLADS Backend is running"}