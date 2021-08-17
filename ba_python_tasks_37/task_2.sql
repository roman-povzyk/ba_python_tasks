SELECT first_name AS First_Name,
        last_name AS Last_Name
FROM employees;


SELECT DISTINCT department_id
FROM employees
ORDER BY department_id;


SELECT *
FROM employees
ORDER BY first_name DESC;


SELECT first_name,
        last_name,
        salary,
        0.12 * salary AS PF
FROM employees;


SELECT MAX(salary) AS max_salary,
		MIN(salary) AS min_salary
FROM employees;


SELECT first_name,
        last_name,
        ROUND(salary, 2) AS month_salary
FROM employees;
