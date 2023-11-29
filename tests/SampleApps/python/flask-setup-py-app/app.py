from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World! {str(datetime.now())}"

