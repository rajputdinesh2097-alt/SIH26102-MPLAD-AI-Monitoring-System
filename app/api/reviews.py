from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    new_review = Review(
        project_id=review.project_id,
        status=review.status,
        comment=review.comment
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


@router.get("/{project_id}")
def get_project_review(
    project_id: int,
    db: Session = Depends(get_db)
):
    review = db.query(Review).filter(
        Review.project_id == project_id
    ).first()

    if not review:
        return {"message": "Review not found"}

    return review

@router.put("/{review_id}")
def update_review(
    review_id: int,
    review: ReviewUpdate,
    db: Session = Depends(get_db)
):
    existing_review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if not existing_review:
        return {"message": "Review not found"}

    existing_review.status = review.status
    existing_review.comment = review.comment

    db.commit()
    db.refresh(existing_review)

    return existing_review