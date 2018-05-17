from middleware.authentication import basic_auth

middlewares = [
    basic_auth
]


def run_middleware(websocket):
    websocket.errors = []
    for middleware in middlewares:
        if callable(middleware):
            websocket = middleware(websocket)
    return websocket
