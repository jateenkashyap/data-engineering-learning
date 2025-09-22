CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO employees (id, name, role, salary) VALUES
(1, 'Alice', 'Data Engineer', 75000.00),
(2, 'Bob', 'Data Analyst', 65000.00),
(3, 'Charlie', 'Data Scientist', 90000.00),
(4, 'Diana', 'Data Engineer', 80000.00);


select * from employees
WHERE role = 'Data Analyst'