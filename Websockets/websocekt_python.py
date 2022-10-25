import asyncio
import websockets
import time
import threading


class Test:

    def __init__(self):
        self._websocket = None

    async def echo(self, websocket):
        self._websocket = websocket
        while 1:
            data = await self._websocket.recv()
        print(data)

    async def main(self):
        async with websockets.serve(self.echo, "localhost", 19955):
            await asyncio.Future()  # run forever


asyncio.run(Test().main())
