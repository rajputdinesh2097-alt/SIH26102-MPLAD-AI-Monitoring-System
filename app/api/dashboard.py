from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.project import Project
from app.models.risk import RiskAnalysis

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    total = db.query(Project).count()

    ongoing = db.query(Project).filter(
        Project.status == "Ongoing"
    ).count()

    completed = db.query(Project).filter(
        Project.status == "Completed"
    ).count()

    delayed = db.query(Project).filter(
        Project.status == "Delayed"
    ).count()

    return {
        "total_projects": total,
        "ongoing_projects": ongoing,
        "completed_projects": completed,
        "delayed_projects": delayed
    }

@router.get("/state-wise")
def state_wise_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    result = {}

    for project in projects:
        state = project.state

        if state not in result:
            result[state] = 0

        result[state] += 1

    return result

@router.get("/district-wise")
def district_wise_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    result = {}

    for project in projects:
        district = project.district

        if district not in result:
            result[district] = 0

        result[district] += 1

    return result

@router.get("/risk-distribution")
def risk_distribution(db: Session = Depends(get_db)):
    high = db.query(RiskAnalysis).filter(
        RiskAnalysis.risk_level == "High"
    ).count()

    medium = db.query(RiskAnalysis).filter(
        RiskAnalysis.risk_level == "Medium"
    ).count()

    low = db.query(RiskAnalysis).filter(
        RiskAnalysis.risk_level == "Low"
    ).count()

    return {
        "high": high,
        "medium": medium,
        "low": low
    }

@router.get("/fund-utilization")
def fund_utilization(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    total_sanctioned = sum(
        project.sanctioned_amount or 0
        for project in projects
    )

    total_expenditure = sum(
        project.expenditure or 0
        for project in projects
    )

    if total_sanctioned == 0:
        utilization = 0
    else:
        utilization = (
            total_expenditure / total_sanctioned
        ) * 100

    return {
        "total_sanctioned": total_sanctioned,
        "total_expenditure": total_expenditure,
        "fund_utilization_percentage": round(utilization, 2)
    }

@router.get("/ai-risk-score")
def ai_risk_score(db: Session = Depends(get_db)):
    risks = db.query(RiskAnalysis).all()

    if not risks:
        return {
            "ai_risk_score": 0,
            "risk_level": "No Data"
        }

    total_score = sum(
        risk.risk_score or 0
        for risk in risks
    )

    average_score = total_score / len(risks)

    if average_score >= 70:
        risk_level = "High Risk"
    elif average_score >= 40:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    return {
        "ai_risk_score": round(average_score, 2),
        "risk_level": risk_level
    }

@router.get("/alert-breakdown")
def alert_breakdown(db: Session = Depends(get_db)):
    risks = db.query(RiskAnalysis).all()

    result = {}

    for risk in risks:
        anomaly = risk.anomaly_type

        if anomaly not in result:
            result[anomaly] = 0

        result[anomaly] += 1

    return result

@router.get("/recent-alerts")
def recent_alerts(db: Session = Depends(get_db)):
    alerts = db.query(RiskAnalysis).order_by(
        RiskAnalysis.id.desc()
    ).limit(10).all()

    return [
        {
            "id": alert.id,
            "project_id": alert.project_id,
            "risk_score": alert.risk_score,
            "risk_level": alert.risk_level,
            "anomaly_type": alert.anomaly_type,
            "reason": alert.reason
        }
        for alert in alerts
    ]

@router.get("/project-monitoring")
def project_monitoring(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    return [
        {
            "id": project.id,
            "project_name": project.project_name,
            "state": project.state,
            "district": project.district,
            "sanctioned_amount": project.sanctioned_amount,
            "expenditure": project.expenditure,
            "progress": project.progress,
            "status": project.status
        }
        for project in projects
    ]

@router.get("/ai-insights")
def ai_insights(db: Session = Depends(get_db)):
    risks = db.query(RiskAnalysis).order_by(
        RiskAnalysis.id.desc()
    ).limit(10).all()

    insights = []

    for risk in risks:
        insights.append({
            "project_id": risk.project_id,
            "risk_level": risk.risk_level,
            "risk_score": risk.risk_score,
            "anomaly_type": risk.anomaly_type,
            "reason": risk.reason
        })

    return {
        "total_insights": len(insights),
        "insights": insights
    }