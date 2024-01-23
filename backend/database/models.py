from . import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Subscription(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
