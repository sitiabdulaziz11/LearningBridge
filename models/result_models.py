from .base_model import Base, BaseClass
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import UserMixin


class Result(Base, BaseClass, UserMixin):
    """Result model that represents result's fields/attributes."""

    __tablename__ = "results"

    Total_score = Column(Float, nullable=False)
    Total_average = Column(Float, nullable=True)
    Rank = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=False, default=datetime.now().strftime("%d-%m-%Y"))
    subject_id = Column(String(20), ForeignKey("subjects.id"), nullable=False)
    student_id = Column(String(20), ForeignKey("students.id"), nullable=False)
    # relation with other tables
    # Q?
    teacher_id = Column(String(20), ForeignKey("teachers.id"), nullable=False)
    # subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    subject_result = relationship("SubjectResult")
    student = relationship("Student", back_populates="results")
    teacher = relationship("Teacher", back_populates="results")
    subject = relationship("Subject", back_populates="results")
