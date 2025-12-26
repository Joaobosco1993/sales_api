from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.schemas import UserCreate, UserRead, Token
from app.crud import create_user, get_user_by_username
from app.auth import verify_password, create_access_token
from app.database import engine
from app.main import get_db, ensure_password_max_bytes

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)
@router.post("/signup", response_model=UserRead)
def signup(
    user_in: UserCreate,
    session: Session = Depends(get_db)
):
    ensure_password_max_bytes(user_in.password)

    existing_user = get_user_by_username(user_in.username, session)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    user = create_user(
        user_in.username,
        user_in.password,
        session
    )

    return UserRead(
        id=user.id,
        username=user.username
    )

