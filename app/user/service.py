from app.user import repository
from app.user.models import UserAccountCreate, UserAccountUpdate
from sqlalchemy.orm import Session


def create(data: UserAccountCreate, db: Session):
    return repository.create(data=data, db=db)


def get_by_id(id: int, db: Session):
    return repository.get_by_id(id=id, db=db)


def update_by_id(id: int, data: UserAccountUpdate, db: Session):
    return repository.update_by_id(id=id, data=data, db=db)


def delete_by_id(id: int, db: Session):
    return repository.delete_by_id(id=id, db=db)



