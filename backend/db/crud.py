from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase
from . import models, schemas


def get_subscription(session: AsyncSession, subscription_id: int):
    return session.get(models.Subscription, subscription_id)


async def get_subscriptions(session: AsyncSession, offset: int = 0, limit: int = 100):
    return db.query(models.Subscription).offset(offset).limit(limit).all()


def create_subscription(db: Session, sub: schemas.SubscriptionCreate):
    db_item = models.Subscription(**sub.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_subscription(db: Session, subscription_id: int):
    sub = db.query(models.Subscription).get(subscription_id)
    if sub:
        db.delete(sub)
        db.commit()
        return True
    else:
        return False

# Users
async def get_user_db(db: Session):
    yield SQLAlchemyUserDatabase(session=db, user_table=models.User)
