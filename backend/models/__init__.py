from sqlalchemy.orm import declarative_base

Base = declarative_base()  # model base class

from .subscription import Subscription
