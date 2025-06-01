from fastapi import FastAPI
from services.cart.interfaces import router as cart_router

app = FastAPI()
app.include_router(cart_router)
