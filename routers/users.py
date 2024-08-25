from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserRequest, UserResponse
from services.db_service import get_db
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/new", response_model=UserResponse)
def create_user(user: Annotated[UserRequest, Body()], db: Session = Depends(get_db)):
    new_db_user = User(**user.model_dump())
    db.add(new_db_user)
    db.commit()
    db.refresh(new_db_user)
    return new_db_user


@router.patch("/update/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: Annotated[UserRequest, Body()], db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_data = user.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    if not db.query(User).filter(User.id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")

    user_to_delete = db.query(User).filter(User.id == user_id)
    user_to_delete.delete()
    db.commit()
    return f"User with id: {user_id} deleted"
