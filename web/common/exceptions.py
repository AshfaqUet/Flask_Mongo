class HttpException(Exception):
    status = None

class BadRequest(HttpException):
    status = 400

    def __init__(self, msg='Invalid Payload'):
        self.msg = msg
