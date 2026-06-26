USE college_db5;

---------------------------------------
-- TASK 1: BASELINE PERFORMANCE – NO INDEXES
---------------------------------------

-- 48
EXPLAIN
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;
-- 49
-- EXPLAIN does not show a Full Table Scan.
-- The enrollments table uses an index (type = index).
-- The students and courses tables use PRIMARY KEY lookups (type = eq_ref).

-- 50
-- Estimated rows examined:
-- enrollments : 10
-- students    : 1
-- courses     : 1
-- Access types:
-- enrollments -> index
-- students    -> eq_ref
-- courses     -> eq_ref
USE college_db5;

---------------------------------------
-- TASK 2: ADD INDEXES AND COMPARE PLANS
---------------------------------------

-- 51
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

-- 52
CREATE UNIQUE INDEX idx_enroll_unique
ON enrollments(student_id, course_id);

-- 53
CREATE INDEX idx_courses_course_name
ON courses(course_name);

-- 54
EXPLAIN
SELECT s.first_name, s.last_name, c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Comparison:
-- students table : ALL (Full Table Scan)
-- enrollments    : ref
-- courses        : eq_ref
-- Query performance improved due to indexes on enrollments and courses.
-- The students table still performs a Full Table Scan.

-- 55
CREATE INDEX idx_enroll_grade_null
ON enrollments(student_id, grade);

-- MySQL does not support partial indexes,
-- so a normal index is created instead.
