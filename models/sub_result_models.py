from .base import Base, Column, Integer, String, ForeignKey, datetime, relationship


class SubjectResult(Base):
    """ Term model that represents term's fields/attributes.
    """
    __tablename__ = "subjectResults"

    id = Column(Integer, primary_key=True)
    test1_score = Column(float(20), nullable=False)
    test2_score = Column(float(20), nullable=False)
    test3_score = Column(float(20))
    assisgnment = Column(float(20), nullable=False)
    worksheer = Column(float(20))
    mid_exam = Column(float(20), nullable=False)
    exer_book = Column(float(20))
    final_exam = Column(float(20), nullable=False)
    totalScore = Column(float(20), nullable=False)
    sub_rank = Column(Integer)
    # term = Column(Integer, ForeignKey("terms.id"), nullable=False)
    # rank = Column(Integer)
    # average = Column(Float)

    # define relationship
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    result_id = Column(Integer, ForeignKey("results.id"), nullable=False)

    # student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
