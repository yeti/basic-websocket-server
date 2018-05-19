from middleware.authentication import basic_auth
from middleware.cleaning import clean_path

middlewares = [
    basic_auth,
    clean_path
]


def run_middleware(websocket):
    for middleware in middlewares:
        if callable(middleware):
            middleware(websocket)
    return websocket
