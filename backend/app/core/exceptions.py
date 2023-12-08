from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InvalidDataException(HTTPException):
    def __init__(self, detail: str = "Invalid data provided"):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail)


exception_handlers: dict = {
    InvalidDataException: (status.HTTP_422_UNPROCESSABLE_ENTITY, "Invalid data provided"),
    NotFoundException: (status.HTTP_404_NOT_FOUND, "Resource not found"),
}
