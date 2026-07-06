Task 1.Create database and tables
CREATE DATABASE college_db;

USE college_db;

CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    hod_name VARCHAR(100) NOT NULL
);

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    professor_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(1),
    UNIQUE(student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO departments (dept_name, hod_name)
VALUES ('CSE', 'Dr. Kumar'), ('ECE', 'Dr. Suresh');

INSERT INTO students (student_name, email, department_id)
VALUES ('Jayasri', 'jaya@gmail.com', 1), ('Arun', 'arun@gmail.com', 2);

INSERT INTO courses (course_name, credits, department_id)
VALUES ('DBMS', 4, 1), ('Networks', 3, 2);

INSERT INTO professors (professor_name, email, department_id)
VALUES ('Dr. Ravi', 'ravi@gmail.com', 1), ('Dr. Meena', 'ravi@gmail.com', 2);

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (1, 1, '2026-06-01', 'A'), (2, 2, '2026-06-02', 'B');

SELECT * FROM departments;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM professors;
SELECT * FROM enrollments;

Task 2: Verify Normalisation
-- 1NF (First Normal Form)
-- All tables contain atomic values.
-- Each column has single value only.
-- No repeating groups or multiple values in a single field.
-- Example: phone numbers are NOT stored in same column.

-- 2NF (Second Normal Form)
-- All tables have single-column primary keys.
-- In enrollments table, (student_id, course_id) is a composite key candidate.
-- Non-key attributes like enrollment_date and grade depend on full key.
-- No partial dependency exists.

-- 3NF (Third Normal Form)
-- No transitive dependency exists in any table.
-- Example: dept_name is not stored in students or courses table.
-- Instead, department_id links to departments table.
-- So dependency is: student_id → department_id → dept_name (removed via normalization)
-- Therefore schema is in 3NF.

-- Enrollments Table Analysis
-- enrollment_id is primary key.
-- student_id and course_id are foreign keys.
-- grade depends only on enrollment record.
-- No attribute depends on another non-key attribute.
-- Hence enrollments table is also in 3NF.

 Task 3: Alter and Extend the Schema

ALTER TABLE students ADD phone_number VARCHAR(15);

ALTER TABLE courses ADD max_seats INT DEFAULT 60;

ALTER TABLE enrollments 
ADD CONSTRAINT chk_grade 
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

ALTER TABLE departments 
RENAME COLUMN hod_name TO head_of_dept;

ALTER TABLE students DROP COLUMN phone_number;

SELECT * FROM students;

SELECT * FROM courses;

SELECT * FROM departments;

SELECT * FROM enrollments;

SELECT * FROM professors;
