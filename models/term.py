from sqlalchemy import Column, String
from .base_model import Base, BaseClass
from flask_login import UserMixin


class Term(BaseClass, Base, UserMixin):
    """Term model that represents term's fields/attributes."""

    __tablename__ = "terms"

    Termname = Column(
        String(100), nullable=False, unique=True
    )  # e.g., "Term 1", "Term 2"
