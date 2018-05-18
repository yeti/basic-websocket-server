from middleware.authentication import basic_auth

middlewares = [
    basic_auth
]


def run_middleware(websocket):
    for middleware in middlewares:
        if callable(middleware):
            middleware(websocket)
    return websocket
