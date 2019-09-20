import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1024)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            from time import sleep
            sleep(5)
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


class KnotsAndCrossesField:

    KNOT = 1
    CROSS = 2

    def __init__(self, field):
        self.field = field

    def _put(self, x, y, type):
        self.field[y][x] = type

    def put_knot(self, x, y):
        self._put(x, y, self.KNOT)

    def put_cross(self, x, y):
        self._put(x, y, self.CROSS)

    def who_won(self):
        for row in self.field:
            row == [self.KNOT] * 3
        for row in self.field:
            row == [self.KNOT] * 3
