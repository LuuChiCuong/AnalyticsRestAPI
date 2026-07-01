from flask import Flask, jsonify
import pymysql
import pandas as pd
import random
from datetime import datetime, timedelta

app = Flask(__name__)
conn = None

def get_conn():
    global conn
    if conn is None:
        conn = pymysql.connect(
            host="myysqldb",
            user="root",
            password="root",
            database="salesdb"
        )
    return conn

def generate_data():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales")
    if cursor.fetchone()[0] > 0:
        return
    products = ["Apple", "Orange", "Banana"]
    start = datetime(2026, 6, 1)
    for i in range(100):
        date = start + timedelta(days=random.randint(0,9))
        product = random.choice(products)
        qty = random.randint(1,20)
        cursor.execute(
            "INSERT INTO sales VALUES (%s,%s,%s)",
            (date.strftime("%Y-%m-%d"), product, qty)
        )
    conn.commit()

@app.route("/analytics")
def analytics():
    generate_data()
    conn = get_conn()
    df = pd.read_sql("""
        SELECT
            saledate,
            productname,
            SUM(quantity) total_quantity,
            AVG(quantity) avg_quantity
        FROM sales
        GROUP BY saledate,productname
        ORDER BY saledate
    """, conn)
    return jsonify(df.to_dict(orient="records"))

app.run(host="0.0.0.0", port=5000)