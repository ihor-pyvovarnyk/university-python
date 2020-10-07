from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from sqlalchemy.orm.exc import NoResultFound

from auth import UserModelIdentity, AdminUserIdentity
from blueprint import api_blueprint
from error_handlers import not_found, server_error

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_URL_RULE'] = '/api/v1/auth'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)

app.register_blueprint(api_blueprint, url_prefix="/api/v1")

app.register_error_handler(NoResultFound, not_found)
app.register_error_handler(Exception, server_error)


def authenticate(username, password):
    from models import Session, Users
    session = Session()
    admin_identity = AdminUserIdentity()
    if username == f'admin-{admin_identity.id}' and password == app.config['SECRET_KEY']:
        return admin_identity
    else:
        user = session.query(Users).filter_by(email=username).first()
        if user and user.password == password:
            return UserModelIdentity(user)


def identity(payload):
    from models import Session, Users
    admin_identity = AdminUserIdentity()
    if payload['identity'] == admin_identity.id:
        return admin_identity
    else:
        session = Session()
        return UserModelIdentity(
            session.query(Users).filter_by(uid=payload['identity']).first()
        )


jwt = JWT(app, authenticate, identity)
