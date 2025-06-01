from fastapi import APIRouter, status
from pydantic import BaseModel

from services.cart.repositories import CartRepo
from services.cart.use_cases import CartUseCases

router = APIRouter()
repo = CartRepo()
use_cases = CartUseCases(repo)


class AddItemRequest(BaseModel):
    item_id: str
    quantity: int


@router.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
async def add_item_to_cart(user_id: str, request: AddItemRequest):
    return use_cases.add_item_to_cart(user_id, request.item_id, request.quantity)


@router.get("/users/{user_id}")
async def get_cart(user_id: str):
    return use_cases.get_cart(user_id)
