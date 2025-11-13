CREATE DATABASE SalesDB

USE SalesDB

CREATE TABLE Products
(
 ProductID INT PRIMARY KEY,
 ProductName NVARCHAR(100),
 Category NVARCHAR(50),
 UnitPrice DECIMAL(10,2)
)

INSERT INTO Products VALUES (1, 'Laptop Xiaomi', 'Electronic', 1200.00)

SELECT * FROM Products

INSERT INTO Products VALUES
(2, 'Wireless Keyboard', 'Electronic', 100),
(3, 'Wireless Mouse', 'Electronic', 50),
(4, 'Table', 'Furniture', 1300),
(5, 'Pen Box', 'Stationary', 15),
(6, 'Chair', 'Furniture', 350),
(7, 'Notebook', 'Stationary', 10)

SELECT * FROM Products

---------------------------------------------------------------------------

CREATE TABLE Sales
(
 SalesID INT PRIMARY KEY IDENTITY,
 ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
 Region NVARCHAR(50) CHECK (Region IN ('East', 'West', 'North', 'South')),
 Quantity INT,
 SalesDate DATE
)

INSERT INTO Sales (ProductID, Region, Quantity, SalesDate) VALUES (1, 'East', 5, '2024-02-23')

SELECT * FROM Sales

INSERT INTO Sales (ProductID, Region, Quantity, SalesDate)
VALUES (3, 'West', 15, '2024-02-23'),
(2, 'East', 10, '2024-02-23'),
(3, 'North', 5, '2024-02-20'),
(4, 'South', 6, '2024-02-24'),
(4, 'West', 10, '2024-03-23'),
(5, 'West', 12, '2024-01-23'),
(6, 'East', 4, '2024-02-24')

SELECT * FROM Products
SELECT * FROM Sales


INSERT INTO Sales (ProductID, Region, Quantity, SaleSDate) VALUES
(1, 'East', 5, '2024-01-10'),
(2, 'West', 10, '2024-01-12'),
(3, 'North', 3, '2024-02-05'),
(4, 'South', 8, '2024-02-10'),
(5, 'East', 2, '2024-03-01'),
(1, 'West', 7, '2024-03-15'),
(3, 'North', 4, '2024-04-03'),
(2, 'South', 6, '2024-04-10'),
(5, 'East', 3, '2024-05-02'),
(4, 'West', 9, '2024-05-10')