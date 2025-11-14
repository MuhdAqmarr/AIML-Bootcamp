CREATE DATABASE EXERCISEONE

USE EXERCISEONE


CREATE TABLE StudentMarks (
    StudentID INT,
    StudentName NVARCHAR(50),
    Math INT,
    Science INT,
    English INT,
    History INT
)

-- INSERT FEW RECORDS
INSERT INTO StudentMarks VALUES
(1, 'Sam', 90, 85, 90,88),
(2, 'Atif', 85, 90, 78, 85),
(3, 'Chang',75, 82, 80, 81),
(4, 'Vi', 70, 85, 72, 65),
(5, 'Ani', 92, 85, 75, 88),
(6, 'Riya', 68, 80, 90, 89)

SELECT * FROM StudentMarks