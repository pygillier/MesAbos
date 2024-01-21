from sqlalchemy.orm import Session
from . import models, schemas


def get_subscription(db: Session, subscription_id: int):
    return db.query(models.Subscription).get(subscription_id)


def get_subscriptions(db: Session, offset: int = 0, limit: int = 100):
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
