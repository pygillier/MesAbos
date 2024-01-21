from fastapi import APIRouter
from backend.routers import subscription

api_router = APIRouter()

api_router.include_router(subscription.router, prefix="/subscriptions")
