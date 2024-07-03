from .base_model import Base, BaseClass
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# Parent - Teacher many-to-many relationship

Parent_teacher = Table(
    "parent_teacher",
    Base.metadata,
    Column("parent_id", String(20), ForeignKey("parents.id")),
    Column("teacher_id", String(20), ForeignKey("teachers.id")),
)


class Parent(BaseClass, Base):
    """Student's Parent Module"""

    __tablename__ = "parents"

    firstname = Column(String(50), nullable=False)
    middlename = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    phone_no = Column(String(60), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    image_file = Column(String(50), unique=True)
    address = Column(String(100), nullable=False)

    # define relation
    teachers = relationship(
        "Teacher", secondary=Parent_teacher, back_populates="parents"
    )
    students = relationship("Student", backref="parent")

    # define relation with Administrator model
    admin_id = Column(String(20), ForeignKey("administrators.id"), nullable=True)
