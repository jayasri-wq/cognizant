use college_db5;
Task 1: Insert, Update and Delete Data

INSERT INTO students (student_name, email, department_id)
VALUES 
('Ravi', 'ravi@college.edu', 1),
('Meena', 'meena@college.edu', 2);


SELECT * FROM students;


UPDATE enrollments
SET grade = 'B'
WHERE student_id = 5 AND course_id = 1;


SELECT * FROM enrollments;


SELECT * FROM enrollments WHERE grade IS NULL;


DELETE FROM enrollments WHERE grade IS NULL;


SELECT COUNT(*) AS total_enrollments FROM enrollments;

---------------------------------------------
 Task 2: Single-Table Queries and Filtering
------------------------------------------------

SELECT * FROM students
ORDER BY student_name;


SELECT * FROM courses
WHERE credits > 3
ORDER BY credits DESC;

SELECT professor_name, email
FROM professors;

SELECT * FROM students
WHERE email LIKE '%@college.edu';


SELECT COUNT(*) AS total_students
FROM students;
--------------------------------
Task 3: Multi-Table Joins
-----------------------------------  
SELECT s.student_name, d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;


SELECT s.student_name, c.course_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;


SELECT s.student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;


SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name;
-----------------------------------------
Task 4: Aggregations and Grouping
------------------------------------
SELECT c.course_name, COUNT(e.student_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name;

SELECT department_id, COUNT(*) AS professor_count
FROM professors
GROUP BY department_id;

SELECT dept_name
FROM departments;

SELECT grade, COUNT(*) AS total
FROM enrollments
WHERE course_id = 1
GROUP BY grade;

SELECT d.department_id, COUNT(s.student_id) AS total_students
FROM departments d
JOIN students s
ON d.department_id = s.department_id
GROUP BY d.department_id
HAVING COUNT(s.student_id) > 2;
