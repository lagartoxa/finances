# -*- coding: utf-8 -*-

from os import path
import sys
import uvicorn




if __name__ == "__main__":
    sys.path.append(path.join(path.dirname(__file__), '..'))
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

