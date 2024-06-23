from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship


class Term(Base):
    """ Term model that represents term's fields/attributes.
    """
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True)
    Termname = Column(String(100), nullable=False,
                      unique=True)  # e.g., "Term 1", "Term 2"
