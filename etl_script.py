import pandas as pd
import pyodbc

# Load Excel
df = pd.read_excel(r'C:\Users\sanch\OneDrive\Desktop\DataEngineering\Sales Data ETL Project\data\Sample-sales-data-excel.xlsx')
df.columns = df.columns.str.strip()  # Clean column names

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Drop rows with missing important fields
df.dropna(subset=['Order Date', 'Sales', 'Quantity'], inplace=True)

# Add Total_Sales
df['Total_Sales'] = df['Sales'] * df['Quantity']

# Convert NaNs to None for SQL compatibility
df = df.where(pd.notnull(df), None)

# Database connection string (Update YOUR details)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=JAVXKS\\SQLEXPRESS;"            # Change to your server name
    "DATABASE=Sales1;"   # Change to your database
    "Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Insert rows
insert_query = """
INSERT INTO Sales (
    [Row ID], [Order ID], [Order Date], [Ship Date], [Ship Mode], [Customer ID], [Customer Name],
    Segment, Country, City, State, [Postal Code], Region, [Product ID], Category,
    [Sub-Category], [Product Name], Sales, Quantity, Discount, Profit, Total_Sales
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded into SQL Server successfully.")
