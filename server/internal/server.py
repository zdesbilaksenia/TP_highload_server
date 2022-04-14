import server.tools.consts as constants

import socket
import os

from server.internal.handler import ServerHandler


class Server:
    def __init__(self, handler: ServerHandler):
        self.handler = handler
        self.socket = None
        self.workers = []

        self.host = constants.HOST
        self.port = constants.PORT
        self.limit_connection = constants.LIMIT_CONNECTIONS
        self.limit_forks = constants.LIMIT_FORKS

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.limit_connection)
        print('Server is listening on ', self.host, ':', self.port)
        self.prefork()

    def prefork(self):
        for thread in range(self.limit_forks):
            pid = os.fork()
            if pid != 0:
                print('New child: ', pid)
                self.workers.append(pid)
            else:
                while True:
                    connection, address = self.socket.accept()

                    try:
                        self.handler.handle(connection)
                    except Exception as exp:
                        print('Error in prefork ', str(exp))

                    connection.close()

        for worker in self.workers:
            os.waitpid(worker, 0)
