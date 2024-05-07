# class ApiException(Exception):

#     def __init__(self, message: str = None, status_code: int = 400):
#         super(ApiException, self).__init__(message)
#         self._message = message
#         self._status_code = status_code

# class BlogIdNotFoundException(ApiException):

#     def __init__(self):
#         super(BlogIdNotFoundException, self).__init__(
#             message="Store not found", status_code=404
#         )

# class TokenNotFoundException():
#     def __init__(self):
#         super(TokenNotFoundException, self).__init__(
#             message="Token not found", status_code=404
#         )
# class OperationalException(Exception):

#     def __init__(self, message: str = None):
#         super(OperationalException, self).__init__(message)
