from flask import Flask
from sqlalchemy.orm.exc import NoResultFound

from blueprint import api_blueprint
from error_handlers import not_found, server_error

app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/api/v1")

app.register_error_handler(NoResultFound, not_found)
app.register_error_handler(Exception, server_error)
