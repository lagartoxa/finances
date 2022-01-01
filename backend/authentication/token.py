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
    authentication_scheme = OAuth2PasswordBearer(tokenUrl="login")

    def __init__(self):
        self.secret_key =\
            "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        self.algorithm = "HS256"
        self.token_expire_min = 30

    def create_token(self, data):
        to_encode = data.copy()
        expire = datetime.utcnow() +\
            timedelta(minutes=self.token_expire_min)
        
        to_encode.update({"exp": expire})
        return jwt.encode(
            to_encode, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token, credentials_exception):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms[self.algorithm, ])
            login: str = payload.get("sub")

            if not login:
                raise credentials_exception
            
            token_data = main.TokenData(username=login)

        except JWTError:
            import traceback
            traceback.print_exc()

            raise credentials_exception

    def get_current_user(self, token: str = Depends(authentication_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer", },
        )

        return self.verify_token(token, credentials_exception)

