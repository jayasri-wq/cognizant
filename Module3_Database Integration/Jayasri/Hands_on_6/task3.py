from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Enrollment

engine = create_engine(
    "mysql+mysqlconnector://root:jaya%40rit@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

"""
TASK 3 - N+1 PROBLEM FIX
"""

# ❌ BEFORE (N+1 problem simulation - concept)
# session.query(Enrollment).all()

# ✅ AFTER (FIX using joinedload)
enrollments = session.query(Enrollment)\
    .options(joinedload(Enrollment.student), joinedload(Enrollment.course))\
    .all()

for e in enrollments:
    print(e.student.student_name, e.course.course_name)

print("N+1 problem fixed using joinedload")