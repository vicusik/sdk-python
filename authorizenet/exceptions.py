
class AuthorizeBase(Exception):
    def __str__(self):
        return self.message

    @property
    def message(self):
        return "Unexpected Authorize.NET exception"


class AuthorizeResponseFailure(AuthorizeBase):
    def __init__(self, http_response):
        self.http_response = http_response

    @property
    def message(self):
        return "Http response code is %s" % self.http_response.status_code


class AuthorizeTransactionFailure(AuthorizeBase):
    def __init__(self, code, text, api_response):
        self.code = code
        self.text = text
        self.api_response = api_response

    @property
    def message(self):
        return "%s: %s" % (self.code, self.text)


class AuthorizeInvalidError(AuthorizeBase):
    def __init__(self, message):
        self._message = message

    @property
    def message(self):
        return self._message
