import asyncio
import websockets

USERS = set()

async def chat(websocket):
    global USERS
    USERS.add(websocket)
    async for message in websocket:
        await asyncio.wait([user.send(message) for user in USERS])

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
