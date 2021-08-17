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

