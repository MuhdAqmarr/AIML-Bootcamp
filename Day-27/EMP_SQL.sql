use OurDB

-- Constraint, not null,
-- primary key: Not null and unique,

CREATE TABLE Emp
(Id INT PRIMARY KEY,
 Fname NVARCHAR(50) NOT NULL,
 Lname NVARCHAR(50)
)

SELECT * FROM Emp

INSERT INTO Emp VALUES ( 1, 'Sam','Dicosta')
INSERT INTO Emp (Id, Fname) VALUES (2, 'Rameez')

-- INSERT INTO Emp (Id, Lname) VALUES (6, 'Marot') : error because Fname cant be null
-- INSERT INTO Emp (Id, Fname) VALUES (2, 'Deep'): Cannot insert duplicate key


DELETE FROM Emp

DROP TABLE Emp

--------------------------------------------------------------------------------------------------

--Default

CREATE TABLE Emp
(Id INT PRIMARY KEY,
 Fname NVARCHAR(50) NOT NULL,
 Lname NVARCHAR(50),
 City NVARCHAR(50) DEFAULT('Kuala Lumpur')
)

SELECT * FROM Emp

INSERT INTO Emp VALUES ( 1, 'Sam','Dicosta', 'Brisbane')
INSERT INTO Emp VALUES ( 2, 'Riha','Kumari', 'Delhi')
INSERT INTO Emp (Id, Fname, Lname) VALUES ( 3, 'Alina','Khan')

-- CHECK
DROP TABLE Emp
CREATE TABLE Emp
(Id INT PRIMARY KEY,
 Fname NVARCHAR(50) NOT NULL,
 Lname NVARCHAR(50),
 City NVARCHAR(50) DEFAULT('Kuala Lumpur'),
 Salary FLOAT NOT NULL CHECK(Salary>=10000 AND Salary<=50000)
)

INSERT INTO Emp (Id, Fname, Lname, Salary) VALUES ( 3, 'Alina','Khan', 12000)

-- INSERT INTO Emp VALUES ( 2, 'Riha','Kumari', 'Delhi', 9000) : The INSERT statement conflicted with the CHECK constraint "CK__Emp__Salary__403A8C7D".
-- The conflict occurred in database "OurDB", table "dbo.Emp", column 'Salary'.
-- INSERT INTO Emp VALUES ( 2, 'Riha','Kumari', 'Delhi', 69000) : The INSERT statement conflicted with the CHECK constraint "CK__Emp__Salary__403A8C7D".
-- The conflict occurred in database "OurDB", table "dbo.Emp", column 'Salary'.
INSERT INTO Emp VALUES ( 2, 'Riha','Kumari', 'Delhi', 19000)


DROP TABLE Emp

CREATE TABLE Emp
(Id INT PRIMARY KEY,
 Fname NVARCHAR(50) NOT NULL,
 Mobile NVARCHAR(10) CHECK (Mobile LIKE'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)

SELECT * FROM Emp

INSERT INTO Emp VALUES ( 1, 'Maan','0123322345')

-- INSERT INTO Emp VALUES ( 2, 'Aiman','0123322a45'): The INSERT statement conflicted with the CHECK constraint "CK__Emp__Mobile__4316F928".
-- The conflict occurred in database "OurDB", table "dbo.Emp", column 'Mobile'.

-- INSERT INTO Emp VALUES ( 3, 'Ain','0123325'): The INSERT statement conflicted with the CHECK constraint "CK__Emp__Mobile__4316F928".
-- The conflict occurred in database "OurDB", table "dbo.Emp", column 'Mobile'.

INSERT INTO Emp (Id, Fname) VALUES ( 3, 'Riya')
INSERT INTO Emp VALUES ( 4, 'Rohan', '0123322345')


-- UNIQUE : Can't duplicate,
DROP TABLE Emp
CREATE TABLE Emp
(Id INT PRIMARY KEY,
 Fname NVARCHAR(50) NOT NULL,
 Mobile NVARCHAR(10) UNIQUE NOT NULL CHECK (Mobile LIKE'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
 Email NVARCHAR(100) UNIQUE
)

SELECT * FROM Emp

INSERT INTO Emp VALUES ( 1, 'Sam', '0123322345', 'sam@yahoo.com')
-- INSERT INTO Emp VALUES ( 2, 'Ravi', '0123322345', 'ravi1256@yahoo.com')
-- Violation of UNIQUE KEY constraint 'UQ__Emp__6FAE0782E24106D4'. Cannot insert duplicate key in object 'dbo.Emp'. 
--The duplicate key value is (0123322345)
INSERT INTO Emp (Id, Fname, Mobile) VALUES ( 3, 'Ravi', '0123322347')

---------------------------------------------------------------------

-- Identity
CREATE TABLE Students
(SId INT IDENTITY,
 SName NVARCHAR(50) NOT NULL,
 SFee FLOAT
)
INSERT INTO Students(SName,SFee) VALUES ('Ravi', 5000.50)
INSERT INTO Students(SName,SFee) VALUES ('Ani', 3000.50)
INSERT INTO Students(SName,SFee) VALUES ('Joy', 4500.20)

SELECT * FROM Students
INSERT INTO Students(SName,SFee) VALUES ('Riya', 4500.20)

---------------------------------------------------------------------

DROP TABLE Students

---------------------------------------------------------------------
CREATE TABLE Students
(SId INT IDENTITY(100,5),
 SName NVARCHAR(50) NOT NULL,
 SFee FLOAT
)
INSERT INTO Students(SName,SFee) VALUES ('Ravi', 5000.50)
INSERT INTO Students(SName,SFee) VALUES ('Ani', 3000.50)
INSERT INTO Students(SName,SFee) VALUES ('Joy', 4500.20)

SELECT * FROM Students
INSERT INTO Students(SName,SFee) VALUES ('Riya', 4500.20)
---------------------------------------------------------------------
CREATE TABLE Salary
(Grade VARCHAR(1) PRIMARY KEY,
 BasicSalary FLOAT,
 HRA AS BasicSalary*0.10 PERSISTED,
 TA AS BasicSalary*0.15 PERSISTED,
 DA AS BasicSalary*0.20 PERSISTED
)

SELECT * FROM Salary
INSERT INTO Salary VALUES ('A', 10000)
INSERT INTO Salary VALUES ('B', 5000)
INSERT INTO Salary VALUES ('C', 2000)
INSERT INTO Salary VALUES ('D', 1000)



SELECT * FROM Salary

SELECT Grade, BasicSalary, BasicSalary+DA+TA+HRA AS 'Net Salary' FROM Salary

SELECT MAX(BasicSalary) AS 'Max Basic' FROM Salary
SELECT MIN(BasicSalary) AS 'Min Basic' FROM Salary
SELECT AVG(BasicSalary) AS 'Average Basic' FROM Salary

-----------------------------------------------------------------------------------------
-- Foreign Key
-----------------------------------------------------------------------------------------

CREATE TABLE Category
(
 CatId INT PRIMARY KEY,
 CategoryName NVARCHAR(50) NOT NULL UNIQUE
)

INSERT INTO Category VALUES (1, 'Electronics'),(2, 'Clothing'),(3, 'Home Decoration'),(4, 'Mobile')
SELECT * FROM Category ORDER BY CatId


CREATE TABLE Products
(
  PId INT PRIMARY KEY IDENTITY,
  PName NVARCHAR(50) NOT NULL,
  PPrice FLOAT NOT NULL,
  ProductCategory INT FOREIGN KEY REFERENCES Category
)

INSERT INTO Products VALUES ('Iphone', 5000, 4),('Nothing 3a', 2000, 4),('Washing Machine', 4000, 1),('Shirt', 200, 2),('T-Shirt', 199, 2), ('Jean', 399, 2)
SELECT * FROM Products
-----------------------------------------------
INSERT INTO Products VALUES('Remote', 209, 5)
-- The INSERT statement conflicted with the FOREIGN KEY constraint "FK__Products__Produc__571DF1D5". The conflict occurred in database "OurDB", table "dbo.
--Category", column 'CatId'
-----------------------------------------------

SELECT * FROM Products
JOIN Category ON Products.ProductCategory = Category.CatId


SELECT * FROM Products p
JOIN Category c ON p.ProductCategory = c.CatId


SELECT p.PId, p.PName, p.PPrice, p.ProductCategory, c.CategoryName FROM Products p
JOIN Category c ON p.ProductCategory = c.CatId


SELECT p.PId 'Product ID', p.PName 'Product Name', p.PPrice 'Product Price', p.ProductCategory 'Product Category',
c.CategoryName 'Category Name' 
FROM Products p 
JOIN Category c 
ON p.ProductCategory = c.CatId







-- ALTER TABLE Emp ADD City NVARCHAR(100) NOT NULL
-- ALTER TABLE Emp DROP COLUMN City
