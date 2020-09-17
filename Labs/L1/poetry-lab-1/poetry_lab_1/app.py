from flask import Flask
app = Flask(__name__)
ASSESSMENT_ID = 3

@app.route(f"/hello-world-{ASSESSMENT_ID}")
def hello_world():
    return f"Hello, World {ASSESSMENT_ID}"