# -*- coding: utf-8 -*-

from datetime import (
    datetime,
    timedelta
)

from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordBearer

from jose import (
    jwt,
    JWTError
)

from backend.schemas.token import TokenDataSchema


AUTHENTICATION_SCHEMA = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY =\
    "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MIN = 30


def create_token(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MIN)

    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM, ])
        login: str = payload.get("sub")

        if not login:
            raise credentials_exception

        token_data = TokenDataSchema(username=login)

    except JWTError:
        import traceback
        traceback.print_exc()

        raise credentials_exception

def get_current_user(token: str = Depends(AUTHENTICATION_SCHEMA)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer", },
    )

    return verify_token(token, credentials_exception)

