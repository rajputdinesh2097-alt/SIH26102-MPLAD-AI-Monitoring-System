from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.project import Project
from app.schemas.project import ProjectCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(
        project_name=project.project_name,
        state=project.state,
        district=project.district,
        sanctioned_amount=project.sanctioned_amount,
        expenditure=project.expenditure,
        progress=project.progress,
        status=project.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return {"message": "Project not found"}

    return project

@router.put("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    existing_project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not existing_project:
        return {"message": "Project not found"}

    existing_project.project_name = project.project_name
    existing_project.state = project.state
    existing_project.district = project.district
    existing_project.sanctioned_amount = project.sanctioned_amount
    existing_project.expenditure = project.expenditure
    existing_project.progress = project.progress
    existing_project.status = project.status

    db.commit()
    db.refresh(existing_project)

    return existing_project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return {"message": "Project not found"}

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}