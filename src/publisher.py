import asyncio
from aioredis import create_connection
import websockets
from custom_protocols.auth import WSServerBasicAuthProtocol


async def publish_to_redis(msg, path):
    conn = await create_connection(('127.0.0.1', 6379))
    await conn.execute(
        'publish',
        '{}'.format(path),
        msg
    )
    conn.close()


async def server(websocket, _):
    try:
        while True:
            message = await websocket.recv()
            await publish_to_redis(message, websocket.path)
            await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosed:
        print('Connection Closed!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    ws_server = websockets.server.serve(
        server,
        '127.0.0.1',
        8765,
        create_protocol=WSServerBasicAuthProtocol
    )
    loop.run_until_complete(ws_server)
    loop.run_forever()
