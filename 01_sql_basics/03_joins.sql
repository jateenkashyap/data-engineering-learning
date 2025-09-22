-- ============================================
-- 01_select_basics.sql
-- Setup + core SELECT patterns in MySQL
-- ============================================

-- 1) Setup (run once to create the demo table)
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employees (id, name, role, salary) VALUES
(1, 'Alice',   'Data Engineer', 75000.00),
(2, 'Bob',     'Data Analyst',  65000.00),
(3, 'Charlie', 'Data Scientist',90000.00),
(4, 'Diana',   'Data Engineer', 80000.00);


CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'Engineering'),
(2, 'Analytics'),
(3, 'Data Science');


ALTER TABLE employees ADD dept_id INT;

UPDATE employees SET dept_id = 1 WHERE role = 'Data Engineer';
UPDATE employees SET dept_id = 2 WHERE role = 'Data Analyst';
UPDATE employees SET dept_id = 3 WHERE role = 'Data Scientist';

SELECT * from employees;

SELECT e.name, e.role, d.dept_name, e.salary
FROM employees e
JOIN departments d
  ON e.dept_id = d.dept_id;

