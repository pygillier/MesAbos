from backend.models import Subscription as SubscriptionDBModel
from backend.schemas.subscription import SubscriptionCreate
from typing import Sequence
from fastapi import HTTPException, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_subscriptions(db_session: AsyncSession, offset: int =0, limit: int =100) -> Sequence[SubscriptionDBModel]:
    subs = (
        await db_session.scalars(
            select(SubscriptionDBModel).limit(limit).offset(offset)
        )
    ).all()
    return subs


async def get_subscription(
    db_session: AsyncSession, sub_id: int
) -> SubscriptionDBModel:
    sub = (
        await db_session.scalars(
            select(SubscriptionDBModel).where(SubscriptionDBModel.id == sub_id)
        )
    ).first()

    if not sub:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return sub


async def create_subscription(db_session: AsyncSession, sub: SubscriptionCreate):
    new_sub = SubscriptionDBModel(**sub.model_dump())
    db_session.add(new_sub)
    await db_session.commit()
    await db_session.refresh(new_sub)
    return new_sub


async def delete_subscription(db_session: AsyncSession, subscription_id: int):
    sub = await get_subscription(db_session=db_session, sub_id=subscription_id)
    await db_session.delete(sub)
    await db_session.commit()
    return Response(status_code=204)
