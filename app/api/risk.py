from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.risk import RiskAnalysis
from app.models.project import Project
from app.schemas.risk import RiskCreate
from app.services.risk_service import calculate_features, calculate_risk

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_risks(db: Session = Depends(get_db)):
    return db.query(RiskAnalysis).all()


@router.post("/")
def create_risk(risk: RiskCreate, db: Session = Depends(get_db)):
    new_risk = RiskAnalysis(
        project_id=risk.project_id,
        risk_score=risk.risk_score,
        risk_level=risk.risk_level,
        anomaly_type=risk.anomaly_type,
        reason=risk.reason
    )

    db.add(new_risk)
    db.commit()
    db.refresh(new_risk)

    return new_risk

@router.get("/high")
def get_high_risks(db: Session = Depends(get_db)):
    return db.query(RiskAnalysis).filter(
        RiskAnalysis.risk_level == "High"
    ).all()

@router.get("/features/{project_id}")
def get_project_features(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        return {"message": "Project not found"}

    return calculate_features(project)

@router.get("/analyze/{project_id}")
def analyze_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        return {"message": "Project not found"}

    features = calculate_features(project)
    risk = calculate_risk(features)

    reason = "; ".join(risk["reasons"])

    if not reason:
        reason = "No anomaly detected"

    anomaly_type = "Rule-Based Risk Analysis"

    existing_risk = db.query(RiskAnalysis).filter(
        RiskAnalysis.project_id == project_id
    ).first()

    if existing_risk:
        existing_risk.risk_score = risk["risk_score"]
        existing_risk.risk_level = risk["risk_level"]
        existing_risk.anomaly_type = anomaly_type
        existing_risk.reason = reason
    else:
        new_risk = RiskAnalysis(
            project_id=project_id,
            risk_score=risk["risk_score"],
            risk_level=risk["risk_level"],
            anomaly_type=anomaly_type,
            reason=reason
        )

        db.add(new_risk)

    db.commit()

    return {
        "project_id": project_id,
        "features": features,
        "risk": risk
    }

@router.get("/{project_id}")
def get_project_risk(
    project_id: int,
    db: Session = Depends(get_db)
):
    risk = db.query(RiskAnalysis).filter(
        RiskAnalysis.project_id == project_id
    ).first()

    if not risk:
        return {"message": "Risk analysis not found"}

    return risk