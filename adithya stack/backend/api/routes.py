from fastapi import APIRouter
from .dependencies import get_current_user
from services.document_service import DocumentService
from services.auth_service import AuthService

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile, user: User = Depends(get_current_user)):
    return await DocumentService.upload_document(file, user)

@router.get("/documents")
async def get_user_documents(user: User = Depends(get_current_user)):
    return await DocumentService.get_user_documents(user.id)

@router.post("/login")
async def login(username: str, password: str):
    return await AuthService.authenticate(username, password)
