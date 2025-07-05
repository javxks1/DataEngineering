--Choose master database to execute DROP commands safely
USE master;
GO

--Look for 'Sales1' database and drop it if it exists
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'Sales1')
BEGIN
    ALTER DATABASE Sales1 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Sales1;
END;

GO

--Create the database
CREATE DATABASE Sales1;

GO

--Use the new database
USE Sales1;

GO

--Look for 'Sales' table and drop it if it exists
IF OBJECT_ID('dbo.Sales', 'U') IS NOT NULL
    DROP TABLE dbo.Sales;

GO

--Create Sales table
CREATE TABLE dbo.Sales (
    [Row ID] INT,
    [Order ID] VARCHAR(50),
    [Order Date] DATE,
    [Ship Date] DATE,
    [Ship Mode] VARCHAR(50),
    [Customer ID] VARCHAR(50),
    [Customer Name] VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    [Postal Code] VARCHAR(20),
    Region VARCHAR(50),
    [Product ID] VARCHAR(50),
    Category VARCHAR(50),
    [Sub-Category] VARCHAR(50),
    [Product Name] VARCHAR(200),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT,
    Total_Sales FLOAT
);

GO
