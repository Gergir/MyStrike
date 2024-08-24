from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all")
def get_all_users():
    pass


@router.get("/{user_id}")
def get_user():
    pass


@router.post("/new")
def create_user():
    pass


@router.patch("/update/{user_id}")
def update_user():
    pass


@router.delete("/delete/{user_id}")
def delete_user():
    pass

