from pydantic import BaseModel, ConfigDict
from enum import Enum
import datetime


class Status(str, Enum):
    active = "active"
    cancelled = "cancelled"
    on_hold = "on hold"


class BillingMode(str, Enum):
    yearly = "yearly"
    monthly = "monthly"


class PaymentMode(str, Enum):
    creditcard = "credit card"
    paypal = "paypal"
    transfer = "transfer"


class SubscriptionBase(BaseModel):

    name: str
    amount: float
    status: Status = Status.active
    billing: BillingMode = BillingMode.monthly
    renewal_date: datetime.date | None = None
    payment: PaymentMode = None
    tags: str = None


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
