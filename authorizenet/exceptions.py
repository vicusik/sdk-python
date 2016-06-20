
class AuthorizeBase(Exception):
    pass


class AuthorizeResponseFailure(AuthorizeBase):
    def __init__(self, http_response):
        self.http_response = http_response


class AuthorizeTransactionFailure(AuthorizeBase):
    def __init__(self, response):
        self.response = response


class AuthorizeInvalidError(AuthorizeBase):
    pass
