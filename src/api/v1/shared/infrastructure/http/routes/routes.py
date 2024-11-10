from fastapi import APIRouter
from src.api.v1.user.infrastructure.http.routes import user_router


router: APIRouter = APIRouter(prefix="/v1")

router.include_router(user_router)
