from models.document import Document
from utils.s3_utils import upload_to_s3
from utils.parsing_utils import parse_document

class DocumentService:
    @staticmethod
    async def upload_document(file, user):
        s3_url = await upload_to_s3(file)
        extracted_text = await parse_document(file)
        document = Document(file_name=file.filename, s3_url=s3_url, user_id=user.id)
        # Save document to the database
        return {"message": "Document uploaded successfully", "url": s3_url}

    @staticmethod
    async def get_user_documents(user_id):
        # Logic to get documents by user
        pass
