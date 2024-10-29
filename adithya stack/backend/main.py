from fastapi import FastAPI
from api.routes import router
from config.logging import configure_logging

app = FastAPI()
configure_logging()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Document Management System API"}
