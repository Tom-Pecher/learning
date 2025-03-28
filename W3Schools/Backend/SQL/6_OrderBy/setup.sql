
-- Setup

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(100),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(100),
    Price DECIMAL
);

INSERT INTO products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES
    (1, 'Chais', 1, 1, '10 boxes x 20 bags', '18'),
    (2, 'Chang', 1, 1, '24 - 12 oz bottles', '19'),
    (3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', '10'),
    (4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', '22'),
    (5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', '21.35');
