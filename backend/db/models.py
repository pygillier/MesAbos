from sqlalchemy import Column, Integer, String, Float, Date

from backend.db.database import Base
from backend.db.schemas import Status, BillingMode


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    amount = Column(Float, default=0)
    status = Column(String(10), default=Status.active)
    billing = Column(String(8), default=BillingMode.monthly)
    renewal_date = Column(Date)
    payment = Column(String(12))
    tags = Column(String(1024))
