from fastapi import APIRouter, status, Response
from pydantic import BaseModel

from services.item.repositories import ItemRepo
from services.item.use_cases import ItemUseCases

router = APIRouter()
repo = ItemRepo()
use_cases = ItemUseCases(repo)


class ItemCreateRequest(BaseModel):
    item_id: str
    name: str


@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(request: ItemCreateRequest, response: Response):
    item = use_cases.create_item(request.item_id, request.name)
    if item is not None:
        return item
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"Item already exists with id {request.item_id}"}


@router.get("/items/")
async def list_items():
    return use_cases.list_items()
