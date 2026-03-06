class ValidationError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class DataBaseNameErr(ValidationError):
    def __init__(self, message="Invalid db name"):
        super().__init__(message,status_code=422)

class UsernameError(ValidationError):
    def __init__(self, message="Invalid username, make sure your username is at least 3 letter long"):
        super().__init__(message, status_code=422)
