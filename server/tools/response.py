from datetime import datetime
import server.tools.consts as constants


class Response:
    def __init__(self, status, request_path="", request_method="", generated_body=""):
        self.headers = None
        self.body = None
        self.content_type = None
        self.content_length = 0
        self.status = None
        self.request_method = request_method

        self.set_status(status, request_path, request_method, generated_body)
        self.generate_headers()

    def generate_headers(self):
        if self.body is not None:
            self.content_length = len(self.body)
        self.headers = f"HTTP/1.1 {self.status}\r\n" + \
                       f"Server: {constants.SERVER}\r\n" + \
                       f"Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')}\r\n" + \
                       f"Connection: keep-alive\r\n" + \
                       f"Content-Length: {self.content_length}\r\n" + \
                       f"Content-Type: {self.content_type}\r\n\r\n"

    def encode(self):
        if self.body is not None and self.request_method != 'HEAD':
            return self.headers.encode() + self.body
        return self.headers.encode()

    def set_status(self, status, path, method, body):
        if status == "200":
            self.status = "200 OK"

            extension = path.split('.')[len(path.split('.')) - 1]
            self.body = body
            self.content_type = constants.CONTENT_TYPE.get(extension)

        if status == "400":
            self.status = '400 Bad Response'

        if status == "403":
            self.status = '403 Forbidden'

        if status == "404":
            self.status = '404 NotFound'

        if status == "405":
            self.status = '405 NotAllowed'
