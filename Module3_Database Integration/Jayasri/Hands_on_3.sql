USE college_db5;

----------------------------
-- TASK 1: SUBQUERIES
----------------------------

-- 35
SELECT s.student_id, s.student_name
FROM students s
WHERE (
    SELECT COUNT(*)
    FROM enrollments e
    WHERE e.student_id = s.student_id
) > (
    SELECT AVG(course_count)
    FROM (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS t
);

-- 36
SELECT c.course_id, c.course_name
FROM courses c
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND (e.grade IS NULL OR e.grade <> 'A')
);

-- 37
SELECT s.student_id, s.student_name
FROM students s
WHERE (
    SELECT COUNT(*)
    FROM enrollments e
    WHERE e.student_id = s.student_id
) = (
    SELECT MAX(course_count)
    FROM (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS t
);

-- 38
SELECT d.department_id, d.dept_name, AVG(t.course_count) AS avg_enrollments
FROM departments d
JOIN (
    SELECT s.department_id, COUNT(e.course_id) AS course_count
    FROM students s
    JOIN enrollments e ON s.student_id = e.student_id
    GROUP BY s.department_id, s.student_id
) t
ON d.department_id = t.department_id
GROUP BY d.department_id, d.dept_name
HAVING AVG(t.course_count) > 2;

---------------------------------------
-- TASK 2: VIEWS
---------------------------------------

-- 39
CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    s.student_id,
    s.student_name,
    s.department_id,
    COUNT(e.course_id) AS total_courses,
    AVG(
        CASE 
            WHEN e.grade = 'A' THEN 4
            WHEN e.grade = 'B' THEN 3
            WHEN e.grade = 'C' THEN 2
            WHEN e.grade = 'D' THEN 1
            WHEN e.grade = 'F' THEN 0
        END
    ) AS gpa
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name, s.department_id;

-- 40
CREATE VIEW vw_course_stats AS
SELECT 
    c.course_id,
    c.course_name,
    COUNT(e.student_id) AS total_enrollments,
    AVG(
        CASE 
            WHEN e.grade = 'A' THEN 4
            WHEN e.grade = 'B' THEN 3
            WHEN e.grade = 'C' THEN 2
            WHEN e.grade = 'D' THEN 1
            WHEN e.grade = 'F' THEN 0
        END
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

-- 41
SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3;

-- 42
UPDATE vw_student_enrollment_summary
SET student_name = 'TEST'
WHERE student_id = 1;

-- 43
DROP VIEW IF EXISTS vw_student_enrollment_summary;
DROP VIEW IF EXISTS vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    student_id,
    student_name,
    department_id
FROM students
WITH CHECK OPTION;



---------------------------------------
TASK 3: STORED PROCEDURES AND TRANSACTIONS
---------------------------------------

-- 44
DELIMITER $$

CREATE PROCEDURE sp_enroll_student (
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    IF EXISTS (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'DUPLICATE ENROLLMENT NOT ALLOWED';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES (p_student_id, p_course_id, p_enrollment_date, NULL);
    END IF;
END $$

DELIMITER ;

-- 45
CREATE TABLE department_transfer_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student (
    IN p_student_id INT,
    IN p_new_department_id INT
)
BEGIN
    DECLARE v_old_department_id INT;

    START TRANSACTION;

    SELECT department_id
    INTO v_old_department_id
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department_id
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (
        student_id,
        old_department_id,
        new_department_id
    )
    VALUES (
        p_student_id,
        v_old_department_id,
        p_new_department_id
    );

    COMMIT;
END $$

DELIMITER ;

-- 46
START TRANSACTION;

UPDATE students
SET department_id = 99999
WHERE student_id = 1;

ROLLBACK;

-- 47
START TRANSACTION;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (1, 1, '2024-01-01', 'A');

SAVEPOINT sp1;

INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES (2, 2, '2024-01-02', 'B');

ROLLBACK TO sp1;

COMMIT;
