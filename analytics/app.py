from flask import Flask
import pymysql
import pandas as pd

app = Flask(__name__)
def get_connection():
    return pymysql.connect(
        host="mysqldb",
        user="root",
        password="root",
        database="salesdb"
    )

@app.route("/analytics")
def analytics():
    conn = get_connection()
    sql = """
    SELECT
        productname,
        AVG(quantity) AS average_per_day,
        SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY productname
    """
    df = pd.read_sql(sql, conn)
    conn.close()
    return df.to_json(orient="records")

app.run(host="0.0.0.0", port=5000)