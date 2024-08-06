import sqlalchemy as sa
from app.user.models import UserAccount, UserAccountCreate, UserAccountUpdate
from sqlalchemy.orm import Session


def create(data: UserAccountCreate, db: Session):
    try:
        query = sa.insert(UserAccount).values(**data.model_dump()).returning(UserAccount)
        response = db.execute(query)
        return response.scalar()
    except Exception:
        return None


def get_by_id(id: int, db: Session):
    query = sa.select(UserAccount).where(UserAccount.id == id)
    response = db.execute(query)
    return response.scalar()


def update_by_id(id: int, data: UserAccountUpdate, db: Session):
    query = (
        sa.update(UserAccount)
        .where(UserAccount.id == id)
        .values(**data.model_dump(exclude_unset=True))
        .returning(UserAccount)
    )
    response = db.execute(query)
    return response.scalar()


def delete_by_id(id: int, db: Session):
    query = sa.delete(UserAccount).where(UserAccount.id == id).returning(UserAccount)
    response = db.execute(query)
    return response.scalar()
