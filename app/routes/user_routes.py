from fastapi import APIRouter, Depends
from ..auth import get_current_user
from ..models import User

router = APIRouter()

# GET CURRENT USER
@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

# DELETE ACCOUNT
@router.delete("/delete-account")
def delete_account(user: User = Depends(get_current_user)):
    db = SessionLocal()
    db.delete(user)
    db.commit()
    return {"message": "Account deleted"}