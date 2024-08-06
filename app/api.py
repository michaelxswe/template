from app.status.controller import router as status_router
from app.user.controller import router as user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(router=user_router)
router.include_router(router=status_router)
