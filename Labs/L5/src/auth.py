import hashlib
from abc import ABC, abstractmethod


class BaseUserIdentity(ABC):
    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def is_admin(self):
        return False


class UserModelIdentity(BaseUserIdentity):
    def __init__(self, model):
        self.model = model

    @property
    def id(self):
        return self.model.uid

    @property
    def is_admin(self):
        return False


class AdminUserIdentity(BaseUserIdentity):
    @property
    def id(self):
        from app import app
        return hashlib.sha256(app.config['SECRET_KEY'].encode()).hexdigest()

    @property
    def is_admin(self):
        return True
