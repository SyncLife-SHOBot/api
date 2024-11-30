from fastapi import APIRouter
from src.api.v1.user.infrastructure.http.routes import user_router
from src.api.v1.inventory.infrastructure.http.routes import inventory_router
from src.api.v1.notes.infrastructure.http.routes import note_router

router: APIRouter = APIRouter(prefix="/v1")

router.include_router(user_router)
router.include_router(inventory_router)
router.include_router(note_router)
