import asyncio
from aioredis import create_connection, Channel
import websockets
from custom_protocols.auth import WSServerBasicAuthProtocol
import os

async def subscribe_to_redis(path):
    conn = await create_connection((os.getenv('REDIS_HOST', 'localhost'), 6379))
    channel = Channel(
        '{}'.format(path),
        is_pattern=False
    )
    await conn.execute_pubsub('subscribe', channel)
    return channel, conn


async def server(websocket, _):
    channel, conn = await subscribe_to_redis(websocket.path)
    try:
        while True:
            message = await channel.get()
            await websocket.send(message.decode('utf-8'))
    except websockets.exceptions.ConnectionClosed:
        await conn.execute_pubsub('unsubscribe', channel)
        conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    import logging
    logger = logging.getLogger('websockets')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    ws_server = websockets.serve(
        server,
        '0.0.0.0',
        8767,
        create_protocol=WSServerBasicAuthProtocol
    )
    loop.run_until_complete(ws_server)
    print('Subscriber initialized!')
    loop.run_forever()
