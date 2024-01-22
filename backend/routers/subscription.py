from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.crud import subscription as crud
from backend.dependencies.core import DBSession
from backend.schemas import subscription as schema
from typing import Any, Sequence

router = APIRouter()


@router.get("/", response_model=Sequence[schema.Subscription])
async def list_subscriptions(db_session: DBSession, offset: int = 0, limit: int = 100):
    subs = await crud.get_subscriptions(db_session=db_session, offset=offset, limit=limit)
    return subs


@router.post("/", response_model=schema.Subscription)
async def create_subscription(sub: schema.SubscriptionCreate, db_session: DBSession):
    sub = await crud.create_subscription(db_session=db_session, sub=sub)
    return sub


@router.get("/{subscription_id}", response_model=schema.Subscription)
async def get_subscription(subscription_id: int, db_session: DBSession) -> Any:
    sub = await crud.get_subscription(db_session=db_session, sub_id=subscription_id)
    return sub


@router.delete("/{subscription_id}")
async def delete_subscription(subscription_id: int, db_session: DBSession):
    return await crud.delete_subscription(db_session=db_session, subscription_id=subscription_id)
