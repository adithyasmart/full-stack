from fastapi import Depends, HTTPException
from models.user import User
from services.auth_service import AuthService

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await AuthService.get_user_from_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
