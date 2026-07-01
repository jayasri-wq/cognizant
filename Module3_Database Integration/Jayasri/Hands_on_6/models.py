from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Database Connection
engine = create_engine(
    "mysql+mysqlconnector://root:jaya%40rit@localhost/college_db_orm",
    echo=True
)

# Department Table
class Department(Base):
    __tablename__ = "department"

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100))

    students = relationship("Student", back_populates="department")


# Student Table
class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(100))
    email = Column(String(100))
    enrollment_year = Column(Integer)

    dept_id = Column(Integer, ForeignKey("department.dept_id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# Course Table
class Course(Base):
    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100))

    enrollments = relationship("Enrollment", back_populates="course")


# Professor Table
class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column(Integer, primary_key=True)
    professor_name = Column(String(100))
    email = Column(String(100))


# Enrollment Table
class Enrollment(Base):
    __tablename__ = "enrollment"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("student.student_id"))
    course_id = Column(Integer, ForeignKey("course.course_id"))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


Base.metadata.create_all(engine)

print("Tables created successfully!")