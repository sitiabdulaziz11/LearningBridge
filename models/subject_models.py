from sqlalchemy import Column, String, ForeignKey
from .student_models import student_subject
from .base_model import Base, BaseClass
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class Subject(Base, BaseClass, UserMixin):
    """Subject model that represents subject's fields/attributes."""

    __tablename__ = "subjects"
    name = Column(String(100), nullable=False, unique=True)

    # Define the relationship to students

    teacher = relationship("Teacher", back_populates="subjects")
    teacher_id = Column(String(20), ForeignKey("teachers.id"), nullable=False)
    students = relationship(
        "Student", secondary=student_subject, back_populates="subjects"
    )
    sub_results = relationship("SubjectResult", backref="subject")
    results = relationship("Result", back_populates="student")
    results = relationship("Result", back_populates="subject")
