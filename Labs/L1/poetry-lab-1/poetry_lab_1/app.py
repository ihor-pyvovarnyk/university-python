from flask import Flask

from poetry_lab_1.blueprint import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix="/api/v1")
