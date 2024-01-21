from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.db import schemas, crud
from typing import Any

router = APIRouter()


@router.get("/", response_model=list[schemas.Subscription])
async def list_subscriptions(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    subscriptions = crud.get_subscriptions(offset=offset, limit=limit, db=db)
    return subscriptions


@router.post("/", response_model=schemas.Subscription)
async def create_subscription(
    sub: schemas.SubscriptionCreate, db: Session = Depends(get_db)
):
    return crud.create_subscription(db=db, sub=sub)


@router.get("/{subscription_id}", response_model=schemas.Subscription)
async def get_subscription(subscription_id: int, db: Session = Depends(get_db)) -> Any:
    sub = crud.get_subscription(db=db, subscription_id=subscription_id)
    if sub:
        return sub
    else:
        raise HTTPException(status_code=404, detail="Subscription not found")


@router.delete("/{subscription_id}")
async def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    if crud.delete_subscription(db=db, subscription_id=subscription_id):
        return {"message": "ok"}
    else:
        return {"message": "ko"}