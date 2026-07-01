from flask import Flask
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("http://analytics:5000/analytics")
    df = pd.DataFrame(r.json())
    pivot = df.pivot(
        index="saledate",
        columns="productname",
        values="total_quantity"
    )
    plt.figure(figsize=(8,4))
    for c in pivot.columns:
        plt.plot(
            pivot.index,
            pivot[c],
            marker="o",
            label=c
        )
    plt.legend()
    plt.xticks(rotation=45)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    graph = base64.b64encode(img.getvalue()).decode()
    return f"""
    <html>
        <body>
            <h2>Sales Analytics</h2>
            {df.to_html(index=False)}
            <img src="data:image/png;base64,{graph}">
        </body>
    </html>
    """
app.run(host="0.0.0.0", port=8000)