from sqlalchemy import Column, String
from .base_model import Base, BaseClass


class Term(BaseClass, Base):
    """ Term model that represents term's fields/attributes.
    """
    __tablename__ = "terms"

    Termname = Column(String(100), nullable=False,
                      unique=True)  # e.g., "Term 1", "Term 2"
