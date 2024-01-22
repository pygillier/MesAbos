from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Date
from datetime import date
from . import Base
from backend.schemas import subscription as schemas


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(10), default=schemas.Status.active)
    billing: Mapped[str] = mapped_column(String(8), default=schemas.BillingMode.monthly)
    renewal_date: Mapped[date]
    payment: Mapped[str] = mapped_column(String(12))
    tags: Mapped[str] = mapped_column(String(1024))
