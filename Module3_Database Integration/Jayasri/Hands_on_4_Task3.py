import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jaya@rit",
    database="college_db5"
)

cursor = conn.cursor()

# ---------------------------------------
# 56. Simulate the N+1 Problem
# ---------------------------------------

print("========== TASK 56 ==========")

query_count = 1

start = time.time()

cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

for row in enrollments:
    student_id = row[1]
    cursor.execute(
        "SELECT student_name FROM students WHERE student_id=%s",
        (student_id,)
    )
    cursor.fetchone()
    query_count += 1

end = time.time()

print("Queries Executed:", query_count)
print("Time Taken:", end - start, "seconds")


# ---------------------------------------
# 57. Rewrite Using a Single JOIN Query
# ---------------------------------------

print("\n========== TASK 57 ==========")

start = time.time()

cursor.execute("""
SELECT e.enrollment_id,
       s.student_name,
       c.course_name,
       e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

end = time.time()

print("Queries Executed: 1")
print("Time Taken:", end - start, "seconds")

print("\nEnrollment Records")

for row in rows:
    print(row)


# ---------------------------------------
# 58. Compare Execution Time
# ---------------------------------------

print("\n========== TASK 58 ==========")

print("N+1 Query Time  :", "See Task 56")
print("JOIN Query Time :", "See Task 57")


# ---------------------------------------
# 59. Document the Difference
# ---------------------------------------

print("\n========== TASK 59 ==========")

print("For 10,000 enrollments:")
print("N+1 approach executes 10,001 queries.")
print("JOIN approach executes only 1 query.")

cursor.close()
conn.close()