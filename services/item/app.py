from fastapi import FastAPI
from services.item.interfaces import router as item_router


app = FastAPI()
app.include_router(item_router)
