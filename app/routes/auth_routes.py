from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, utils, auth
from ..database import SessionLocal
import random

router = APIRouter()

verification_codes = {}  # TEMP storage

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# REGISTER
@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(400, "Email already exists")

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=utils.hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

# LOGIN
@router.post("/login")
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()

    if not user or not utils.verify_password(data.password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = auth.create_access_token({"user_id": user.id})

    return {"access_token": token, "token_type": "bearer"}

# SEND CODE
@router.post("/send-code")
def send_code(email: str):
    code = str(random.randint(100000, 999999))
    verification_codes[email] = code
    return {"message": "Code sent", "code": code}  # simulate email

# VERIFY
@router.post("/verify")
def verify(data: schemas.VerifyCode, db: Session = Depends(get_db)):
    if verification_codes.get(data.email) != data.code:
        raise HTTPException(400, "Invalid code")

    user = db.query(models.User).filter(models.User.email == data.email).first()
    user.is_verified = True
    db.commit()

    return {"message": "Account verified"}