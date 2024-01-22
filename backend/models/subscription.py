from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from . import Base
from backend.schemas import subscription as schemas


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    amount: Mapped[float]
    status: Mapped[str] = mapped_column(default=schemas.Status.active)
    billing: Mapped[str] = mapped_column(default=schemas.BillingMode.monthly)
    renewal_date: Mapped[date]
    payment: Mapped[str]
    tags: Mapped[str]
