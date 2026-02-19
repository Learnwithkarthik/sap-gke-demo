from flask import Flask, render_template_string
import requests
import os

app = Flask(__name__)

API_URL = os.getenv("API_URL", "http://sap-api-service:80/api")

@app.route("/")
def index():
    try:
        response = requests.get(API_URL)
        data = response.json()
    except:
        data = {"message": "API not reachable"}

    html = """
    <h1>SAP Web Application</h1>
    <p><b>Backend Response:</b></p>
    <pre>{{ data }}</pre>
    """

    return render_template_string(html, data=data)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
