from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user

from schemas.jobs import JobCreate
from db.models.jobs import Job
from db.models.users import User

def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retrieve_job(id: int, db: Session):
    job = db.query(Job).filter(Job.id == id).first()
    return job


def list_jobs(db: Session):
    jobs = db.query(Job).filter(Job.is_active==True).all()
    return jobs


def update_job_by_id(id: int, job: JobCreate, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0

    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1


def delete_job_by_id(id: int, db: Session, current_user: User):
    existing_job = db.query(Job).filter(Job.id == id)

    if not existing_job.first():
        return 0
    
    if existing_job.owner_id != current_user.id and not current_user.is_superuser:
        return 0

    existing_job.delete()
    db.commit()
    return 1