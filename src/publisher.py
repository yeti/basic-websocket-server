import asyncio
from aioredis import create_connection, Channel
import websockets

async def publish_to_redis(msg, path):
	conn = await create_connection(('127.0.0.1', 6379))
	await conn.execute(
		'publish',
		'{}'.format(path),
		msg
		)
	conn.close()

async def server(websocket, path):
	try:
		while True:
			message = await websocket.recv()
			await publish_to_redis(message, path)
			await asyncio.sleep(1)
	except websockets.exceptions.ConnectionClosed:
		print('Connection Closed!')


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.set_debug(True)
	ws_server = websockets.serve(
		server,
		'127.0.0.1',
		8765)
	loop.run_until_complete(ws_server)
	loop.run_forever()
