from flask import Flask
import requests
import pandas as pd

app = Flask(__name__)
@app.route("/")
def home():
    r = requests.get("http://analytics:5000/analytics")
    df = pd.DataFrame(r.json())
    return df.to_html(index=False)
app.run(host="0.0.0.0", port=8000)