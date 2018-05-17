from websockets.server import WebSocketServerProtocol
from middleware import run_middleware
from http import HTTPStatus
from json import dumps


class WSServerBasicAuthProtocol (WebSocketServerProtocol):

    DOCSTRING = '''
    Override to process authentication middleware
    '''

    async def process_request(self, *args):
        _, request_headers = args
        processed_protocol = run_middleware(self)
        if len(processed_protocol.errors) > 0:
            return (
                HTTPStatus.UNAUTHORIZED.value,
                [],
                bytes('Errors: {}'.format(dumps(processed_protocol.errors)), 'utf-8')
            )
