from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship


class Result(Base):
    """ Result model that represents result's fields/attributes.
    """
    __tablename__ = "results"
    
    id = Column(Integer, primary_key=True)
    Total_score = Column(float, nullable=False)
    Total_average = Column(float, nullable=True)
    Rank = Column(Integer, nullable=True)
    date = Column(datetime, nullable=False, default=datetime.now().strftime('%d-%m-%Y'))
    
    
    # relation with other tables
    subject_result = relationship("SubjectResult", backref="subject")
    # Q?
    student = relationship("Student", back_populates="results")
    teacher = relationship("Teacher", back_populates="results")
    # subject = relationship("Subject", back_populates="results")
    # student_id = Column(Integer, ForeignKey("students.id"), nullable=False) # Each result is linked to one student or for specific student
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False) # who is the teacher or home room teacher
    # subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
   