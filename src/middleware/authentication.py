from os import getenv
from re import search
from passlib.hash import argon2
from base64 import b64decode

WRONG_NUM_AUTH_TOKEN_ERROR = 'Wrong number of Authorization headers'
NOT_BASIC_AUTH_ERROR = 'No Basic Auth Found'
BAD_AUTH_TOKEN_ERROR = 'Bad Authorization Token'


def _compare_tokens(b64_token1, argon2_token2):
    token1 = b64decode(bytes(b64_token1, 'utf-8')).decode('utf-8')
    return argon2.verify(token1, argon2_token2)


def basic_auth(websocket):
    our_token = getenv('AUTHORIZATION_TOKEN')
    if our_token is not None:
        authorization = websocket.request_headers.get_all('Authorization')
        if authorization is not None and len(authorization) == 1:
            token_search = search(r'^Basic (.+)$', authorization[0])
            if token_search is not None:
                token = token_search.group(1)
                if _compare_tokens(token, our_token):
                    return websocket
                else:
                    websocket.errors.append(BAD_AUTH_TOKEN_ERROR)
            else:
                websocket.errors.append(NOT_BASIC_AUTH_ERROR)
        else:
            websocket.errors.append(WRONG_NUM_AUTH_TOKEN_ERROR)
    return websocket
