from fastapi import APIRouter, status, Response
from pydantic import BaseModel

from services.user.repositories import UserRepo
from services.user.use_cases import UserUseCases

router = APIRouter()
repo = UserRepo()
use_cases = UserUseCases(repo)


class UserCreateRequest(BaseModel):
    user_id: str
    name: str


@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(request: UserCreateRequest, response: Response):
    user = use_cases.create_user(request.user_id, request.name)
    if user is not None:
        return user
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {"error": f"User already exists with id {request.user_id}"}

