-- Create a table of your choice inside the sample SQLite database, rename it,
-- and add a new column. Insert a couple rows inside your table.
-- Also, perform UPDATE and DELETE statements on inserted rows.

-- As a solution to this task, create a file named:
-- task1.sql, with all the SQL statements you have used to accomplish this task


CREATE TABLE grocerries (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER
);

ALTER TABLE grocerries
RENAME TO my_products;

ALTER TABLE my_products
ADD price FLOAT;

INSERT INTO grocerries VALUES
        ('Milk', 20, 25),
        ('Meat', 25, 65),
        ('Apples', 52, 78);

UPDATE grocerries SET name = 'Vegan Meat'
WHERE id = 2;

DELETE FROM grocerries
WHERE id = 3;

