from app.database.core import get_db
from app.user import service
from app.user.models import UserAccountCreate, UserAccountRead, UserAccountUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(path="")
def create(data: UserAccountCreate, db: Session = Depends(get_db)):
    new_user_account = service.create(data=data, db=db)
    if not new_user_account:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return new_user_account


@router.get(path="/{id}", response_model=UserAccountRead)
def get_by_id(id: int, db: Session = Depends(get_db)):
    selected_user_account = service.get_by_id(id=id, db=db)
    if not selected_user_account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return selected_user_account


@router.patch(path="/{id}", response_model=UserAccountRead)
def update_by_id(id: int, data: UserAccountUpdate, db: Session = Depends(get_db)):
    updated_user_account = service.update_by_id(id=id, data=data, db=db)
    if not updated_user_account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return updated_user_account


@router.delete(path="/{id}", response_model=UserAccountRead)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    deleted_user_account = service.delete_by_id(id=id, db=db)
    if not deleted_user_account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return deleted_user_account
