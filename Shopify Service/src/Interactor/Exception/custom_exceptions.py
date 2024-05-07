class ApiException(Exception):

    def __init__(self, message: str = None, status_code: int = 400):
        super(ApiException, self).__init__(message)
        self._message = message
        self._status_code = status_code

    @property
    def error_message(self):

        if self._message is None:
            return "An error occurred"

        return self._message

    @property
    def status_code(self):

        if self._status_code is None:
            return 500

        return self._status_code


class OperationalException(Exception):

    def __init__(self, message: str = None):
        super(OperationalException, self).__init__(message)


class NoDataProvidedApiException(ApiException):

    def __init__(self):
        super(NoDataProvidedApiException, self).__init__(
            message="No data provided", status_code=400
        )


class ClientException(Exception):

    def __init__(self, message: str = None):
        super(ClientException, self).__init__(message)

class MappingException(Exception):

    def __init__(self, message: str = None):
        super(MappingException, self).__init__(message)
        
# Invalid API key or access token (unrecognized login or wrong password)
class UnauthorizedApiException(ApiException):

    def __init__(self):
        super(UnauthorizedApiException, self).__init__(
            message="Invalid API key or access token", status_code=401
        )
        
# Store not found in database
class StoreNotFoundException(ApiException):

    def __init__(self):
        super(StoreNotFoundException, self).__init__(
            message="Store not found", status_code=404
        )
        
# New exception for Shopify API errors
class ShopifyAPIException(ApiException):

    def __init__(self, message: str = "Shopify API error", status_code: int = 500):
        super(ShopifyAPIException, self).__init__(message, status_code)
        