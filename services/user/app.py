from fastapi import FastAPI
from services.user.interfaces import router as user_router

app = FastAPI()
app.include_router(user_router)
