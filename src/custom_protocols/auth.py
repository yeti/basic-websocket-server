from websockets.server import WebSocketServerProtocol
from middleware import run_middleware
from http import HTTPStatus
from json import dumps


class WSServerBasicAuthProtocol (WebSocketServerProtocol):

    DOCSTRING = '''
    Override to process authentication middleware
    '''

    errors = []

    async def process_request(self, *args):
        _, request_headers = args
        run_middleware(self)
        if len(self.errors) > 0:
            return (
                HTTPStatus.UNAUTHORIZED.value,
                [],
                bytes('Errors: {}'.format(dumps(self.errors)), 'utf-8')
            )
