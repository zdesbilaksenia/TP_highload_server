from urllib.parse import unquote

import server.tools.consts as consts
import os

from server.tools.request import Request
from server.tools.response import Response


class ServerHandler:
    def read_file(self, path):
        with open(path, 'rb') as f:
            body = f.read()
        return body

    def handle(self, sock):
        bytes = b''
        while not bytes.endswith(b'\n'):
            bytes += sock.recv(1024)

        data = bytes.decode()
        request = Request(data)

        if request.method not in consts.ALLOWED_METHODS:
            sock.sendall(Response("405").encode())
            return

        if request.status != "ok":
            sock.sendall(Response("400").encode())
            return

        if '/../' in request.path:
            sock.sendall(Response("403").encode())
            return

        request.path = unquote(request.path.split('?')[0])

        request.path = os.getcwd() + request.path

        if os.path.isdir(request.path):
            request.path += 'index.html'
            if not os.path.isfile(request.path):
                sock.sendall(Response("403").encode())
                return

        if not os.path.exists(request.path):
            sock.sendall(Response("404").encode())
            return

        try:
            body = self.read_file(request.path)
        except Exception as exp:
            print('Error in body', str(exp))
            return

        sock.sendall(Response("200", request.path, request.method, body).encode())
