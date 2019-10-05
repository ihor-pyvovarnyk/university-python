class Authorizer:
    def __init__(self, connection):
        self.connection = connection

    def authorize(self, username, password):
        ...

class System:
    def __init__(self, authorizer):
        self.authorizer = authorizer

    def is_running(self):
        ...

    def schedule_appointment(self, request):
        if self.authorizer.authorize(request.username, request.password):
            ...
