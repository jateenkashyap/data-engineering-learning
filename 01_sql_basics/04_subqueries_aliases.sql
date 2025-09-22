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


-- 1) Find employees earning more than the average salary
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary) FROM employees
);

-- 2) Use an alias to rename columns for cleaner output
SELECT e.name AS employee_name, e.role AS job_title, e.salary AS yearly_salary
FROM employees e;

-- 3) Subquery inside SELECT: show salary vs average salary
SELECT name,
       salary,
       (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;



