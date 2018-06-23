import asyncio
from aioredis import create_connection
import websockets
from custom_protocols.auth import WSServerBasicAuthProtocol
import os

async def publish_to_redis(msg, path):
    conn = await create_connection((os.getenv('REDIS_HOST', 'localhost'), 6379))
    await conn.execute(
        'publish',
        '{}'.format(path),
        '{}'.format(msg)
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
    import logging
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    ws_server = websockets.server.serve(
        server,
        '0.0.0.0',
        8765,
        create_protocol=WSServerBasicAuthProtocol
    )
    loop.run_until_complete(ws_server)
    print('Publisher Initialized')
    loop.run_forever()
