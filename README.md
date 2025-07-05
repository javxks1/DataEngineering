
# Sample Sales Data ETL Pipeline

## Project Overview 
A simple ETL pipeline that extracts data from an sample data Excel file, transforms it using pandas, and loads it into a SQL Server Management Studio database.


## Explanation
-This script loads the excel file first.<br/>
-Start transforming by converting dates.<br/>
-Rows with important information (which cannot be null) are dropped. <br/>
-New total sales column creation by multiplying the Sales and Quantity columns.<br/>
-Convert NaNs into None for SQL compatibility.<br/>
-Establish connection with Microsoft SQL Server database. <br/>
-Create new database and insert new rows.<br/>
-Commit to changes.<br/>



## Tools
-Python (Visual Studio) <br/>
-Python extensions - _Pandas for data analysis & Pyodbc for databases connections._ <br/>
-Microsoft SQL Server Management Studio<br/>

## Instructions
1. Install Python 
Make sure you install Python 3. x.
Download: https://www.python.org/downloads/<br/>
2. Download the Project
Download the project files from this git.<br/>
3. Install Required Python Packages
Make sure you have the following packages:
•	pandas
•	pyodbc
•	openpyxl

If not, you can install all the needed extensions using commands:
*Open the python terminal and type these commands*
a. pip install pandas 
b. pip install pyodbc 
c. pip install openpyxl<br/>

4. Set Up SQL Server
•	Open SQL Server Management Studio (SSMS).
•	Create a SQL Server instance if not already running.
•	Make sure TCP/IP is enabled for remote/local connections.
•	Remember your server’s name (yourlocalhost\\SQLEXPRESS) and credentials.<br/>

5. Update Connection String in Script
In etl_script.py, make sure to edit your connection string (conn_str) for a connection with your local database, example:
When using Windows Authentication:
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=master;" 
    "Trusted_Connection=yes;" 
)
If using SQL Server Authentication type your username and password:
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=master;"
    "UID=your_username;"
    "PWD=your_password;"
)<br/>

6. Place Excel File in Data Folder
Ensure the excel file is inside the correct folder and the file path is correctly set in the script:
Example: ‘C:\Users\user\DataEngineering\Sales Data ETL Project\data\Sample-sales-data-excel.xlsx’<br/>

7. Run the SQL Script
Look for the sales.sql script file and open it on SSMS. Then run the script. 
This script should allow you to create a new Sales1 database and a new Sales table where the ETL process. <br/>

8. Run the ETL Script
Open a terminal and run the following command:
python etl_script.py

or use any python environment software and run this script.<br/>

9. Verify the Data in SQL Server
Open SSMS, connect to your server and check that the new database and table have been created. Run SELECT * FROM Sales; to view inserted data.
<br/>
