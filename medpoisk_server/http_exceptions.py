from fastapi import HTTPException, status

InternalErorr = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)

UnauthorizedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User not authorized",
    headers={"WWW-Authenticate": "Bearer"},
)
