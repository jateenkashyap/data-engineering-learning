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


-- Count employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Average salary by role
SELECT role, AVG(salary) AS avg_salary
FROM employees
GROUP BY role;

-- Highest salary
SELECT MAX(salary) AS highest_salary
FROM employees;

