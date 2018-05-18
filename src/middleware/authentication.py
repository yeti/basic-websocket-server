from os import getenv
from passlib.hash import argon2
from base64 import b64decode
from re import search

BAD_AUTH_TOKEN_ERROR = 'Bad Authorization Token'
NO_TOKEN_RECEIVED = 'Authorization token not received'

TOKEN_PATTERN = r'\?.*token\=([^&/]+)'


def _compare_tokens(b64_token1, argon2_token2):
    token1 = b64decode(bytes(b64_token1, 'utf-8')).decode('utf-8')
    result = argon2.verify(token1, argon2_token2)
    return result


def basic_auth(websocket):
    our_token = getenv('AUTHORIZATION_TOKEN')
    token_search = search(TOKEN_PATTERN, websocket.path)
    if our_token is not None:
        if token_search is not None:
            authorization = token_search.group(1)
            if _compare_tokens(authorization, our_token):
                return websocket
            else:
                websocket.errors.append(BAD_AUTH_TOKEN_ERROR)
        else:
            websocket.errors.append(NO_TOKEN_RECEIVED)
    if token_search is not None:
        root_path = websocket.path.split('?')[0]
        websocket.path = root_path
    return websocket
