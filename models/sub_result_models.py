from sqlalchemy import Column, String, ForeignKey, Float
from .base_model import BaseClass, Base
from flask_login import UserMixin


class SubjectResult(Base, BaseClass, UserMixin):
    """Term model that represents term's fields/attributes."""

    __tablename__ = "subjectResults"

    test1_score = Column(Float(20), nullable=False)
    test2_score = Column(Float(20), nullable=False)
    test3_score = Column(Float(20))
    assisgnment = Column(Float(20), nullable=False)
    worksheer = Column(Float(20))
    mid_exam = Column(Float(20), nullable=False)
    exer_book = Column(Float(20))
    final_exam = Column(Float(20), nullable=False)
    totalScore = Column(Float(20), nullable=False)
    sub_rank = Column(String(20))
    # term = Column(Integer, ForeignKey("terms.id"), nullable=False)
    # rank = Column(Integer)
    # average = Column(Float)

    # define relationship
    subject_id = Column(String(20), ForeignKey("subjects.id"), nullable=False)
    result_id = Column(String(20), ForeignKey("results.id"), nullable=False)

    # student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
