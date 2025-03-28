
-- Setup

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    CustomerID SERIAL PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Address VARCHAR(100),
    City VARCHAR(100),
    PostalCode VARCHAR(100),
    Country VARCHAR(100)
);

INSERT INTO customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES
-- CustomerID, CustomerName,                    ContactName,            Address,                            City,           PostalCode, Country
    (1, 'Alfreds Futterkiste',                  'Maria Anders',         'Obere Str. 57',                    'Berlin',       '12209',    'Germany'),
    (2, 'Ana Trujillo Emparedados y helados',   'Ana Trujillo',         'Avda. de la Constitución 2222',    'México D.F.',  '05021',    'Mexico'),
    (3, 'Antonio Moreno Taquería',              'Antonio Moreno',       'Mataderos 2312',                   'México D.F.',  '05023',    'Mexico'),
    (4, 'Around the Horn',                      'Thomas Hardy',         '120 Hanover Sq.',                  'London',       'WA1 1DP',  'UK'),
    (5, 'Berglunds snabbköp',                   'Christina Berglund',   'Berguvsvägen 8',                   'Luleå',        'S-958 22', 'Sweden');
