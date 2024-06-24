from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship
from student_models import student_subject


class Subject(Base):
    """ Subject model that represents subject's fields/attributes.
    """
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    
    # Define the relationship to students
    
    teacher = relationship("Teacher", back_populates="subjects")
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    students = relationship("Student", secondary=student_subject, back_populates="subjects")
    sub_results = relationship("SubjectResult", backref="subject")
    