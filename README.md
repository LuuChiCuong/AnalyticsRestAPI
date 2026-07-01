# AnalyticsRestAPI

Write a simple demo program using Docker Compose to meet the following requirements:
1. There are three services: myysqldb, analytics, and dashboard.
2. myysqldb runs in MySQL, analytics, and dashboard run in Python.
3. myysqldb has a sales table with fields: date, productname, and quantity. There are 100 records for three product types, covering a 10-day period. The data is simulated.
4. analytics accesses myysqldb's sales table and calculates the average daily sales per product (productname) and the total sales per product (quantity by productname).
5. The analytics calculation results are returned as a pandas dataframe.
6. dashboard receives the analytics results via a REST API and outputs them to the screen.
