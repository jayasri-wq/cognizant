from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Department, Student, Course, Enrollment

engine = create_engine(
    "mysql+mysqlconnector://root:jaya%40rit@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# -------------------------
# 81. INSERT Departments
# -------------------------
d1 = Department(dept_id=1, dept_name="Computer Science")
d2 = Department(dept_id=2, dept_name="Electronics")
d3 = Department(dept_id=3, dept_name="Mechanical")

session.add_all([d1, d2, d3])
session.commit()

# -------------------------
# 82. INSERT Students
# -------------------------
s1 = Student(student_id=1, student_name="A", email="a@gmail.com", enrollment_year=2022, dept_id=1)
s2 = Student(student_id=2, student_name="B", email="b@gmail.com", enrollment_year=2023, dept_id=1)
s3 = Student(student_id=3, student_name="C", email="c@gmail.com", enrollment_year=2022, dept_id=2)
s4 = Student(student_id=4, student_name="D", email="d@gmail.com", enrollment_year=2021, dept_id=3)
s5 = Student(student_id=5, student_name="E", email="e@gmail.com", enrollment_year=2024, dept_id=2)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

# -------------------------
# 82. INSERT Courses
# -------------------------
c1 = Course(course_id=1, course_name="DBMS")
c2 = Course(course_id=2, course_name="Python")
c3 = Course(course_id=3, course_name="AI")

session.add_all([c1, c2, c3])
session.commit()

# -------------------------
# 82. INSERT Enrollments
# -------------------------
e1 = Enrollment(enrollment_id=1, student_id=1, course_id=1)
e2 = Enrollment(enrollment_id=2, student_id=2, course_id=2)
e3 = Enrollment(enrollment_id=3, student_id=3, course_id=3)
e4 = Enrollment(enrollment_id=4, student_id=1, course_id=2)

session.add_all([e1, e2, e3, e4])
session.commit()

# -------------------------
# 83. READ (JOIN)
# -------------------------
students_cs = session.query(Student).join(Department).filter(
    Department.dept_name == "Computer Science"
).all()

for s in students_cs:
    print(s.student_name, s.email)

# -------------------------
# 84. READ enrollments
# -------------------------
enrollments = session.query(Enrollment).all()

for e in enrollments:
    print(e.student.student_name, e.course.course_name)

# -------------------------
# 85. UPDATE student email match
# -------------------------
student = session.query(Student).filter_by(email="a@gmail.com").first()
if student:
    student.enrollment_year = 2025
    session.commit()

# -------------------------
# 86. DELETE enrollment
# -------------------------
enrollment = session.query(Enrollment).first()
session.delete(enrollment)
session.commit()

print("CRUD Operations Completed")