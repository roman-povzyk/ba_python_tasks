-- Use the sample SQLite database hr.db

-- As a solution to HW, create a file named: task2.sql with all SQL queries:

-- 1. write a query to display the names (first_name, last_name) using alias name "First Name",
-- "Last Name" from the table of employees;

SELECT first_name AS First_Name,
        last_name AS Last_Name
FROM employees;

-- 2. write a query to get the unique department ID from the employee table

SELECT DISTINCT department_id
FROM employees
ORDER BY department_id;

-- 3. write a query to get all employee details from the employee table ordered by first name, descending

SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. write a query to get the names (first_name, last_name), salary,
-- PF of all the employees (PF is calculated as 12% of salary)

SELECT first_name,
        last_name,
        salary,
        0.12 * salary AS PF
FROM employees;

-- 5. write a query to get the maximum and minimum salary from the employees table

SELECT MAX(salary) AS max_salary,
		MIN(salary) AS min_salary
FROM employees;

-- 6. write a query to get a monthly salary (round 2 decimal places) of each and every employee

SELECT first_name,
        last_name,
        ROUND(salary, 2) AS month_salary
FROM employees;
