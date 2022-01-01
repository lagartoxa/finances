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


class LocalAuthentication():
    SECRET_KEY =\
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def create_token(self, data):
        to_encode = data.copy()
        expire = datetime.utcnow() +\
            timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        return jwt.encode(
            to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token, credentials_exception):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms[ALGORITHM, ])
            login: str = payload.get("sub")

            if not login:
                raise credentials_exception
            
            token_data = main.TokenData(username=login)

        except JWTError:
            import traceback
            traceback.print_exc()

            raise credentials_exception

    def get_oauth_scheme(self):
        return OAuth2PasswordBearer(tokenUrl="login")

    def get_current_user(self, token: str = Depends(self.get_oauth_scheme())):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer", },
        )

        return self.verify_token(token, credentials_exception)

