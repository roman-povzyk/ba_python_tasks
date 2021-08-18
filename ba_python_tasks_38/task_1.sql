-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)
-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- 1. write a query in SQL to display the first name, last name, department number,
-- and department name for each employee

SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN department d
	ON e.department_id = d.department_id;

-- 2. write a query in SQL to display the first and last name,
-- department, city, and state province for each employee

SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
FROM employees e
JOIN department d
	ON e.department_id = d.department_id
JOIN locations l
	ON d.location_id = l.location_id;

-- 3. write a query in SQL to display the first name, last name,
-- department number, and department name, for all employees for departments 80 or 40

SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
JOIN department d
	ON e.department_id = d.department_id
WHERE e.department_id = 40 OR e.department_id = 80;

-- 4. write a query in SQL to display all departments including those where does not have any employee

SELECT department_id, department_name
FROM department;

-- 5. write a query in SQL to display the first name of all employees including the first name of their manager

SELECT e1.first_name AS employee_first_name,
		e2.first_name AS manager_first_name
FROM employees e1
JOIN employees e2
	ON e1.manager_id = e2.employee_id
ORDER BY manager_first_name;

-- 6. write a query in SQL to display the job title, full name (first and last name )
-- of the employee, and the difference between the maximum salary for the job and the salary of the employee

SELECT j.job_title, e.first_name, e.last_name, j.max_salary - e.salary AS difference_salary
FROM employees e
JOIN jobs j
	ON e.job_id = j.job_id
ORDER BY difference_salary;

-- 7. write a query in SQL to display the job title and the average salary of employees

SELECT j.job_title,
		AVG(salary) AS avg_salary
FROM employees e
JOIN jobs j
	ON e.job_id = j.job_id
GROUP BY job_title
ORDER BY avg_salary;

-- 8. write a query in SQL to display the full name (first and last name),
-- and salary of those employees who work in any department located in London

SELECT e.first_name, e.last_name, e.salary
FROM employees e
JOIN department d
	ON e.department_id = d.department_id
JOIN locations l
	ON d.location_id = l.location_id
WHERE l.city = 'London';

-- 9. write a query in SQL to display the department name and the number of employees in each department
SELECT d.department_name, COUNT(*) AS employees_department
FROM department d
JOIN employees e
	ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY employees_department;
