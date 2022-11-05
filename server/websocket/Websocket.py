import asyncio
import websockets, json
from text_format.format_text_to_function import TextFormat

async def handler(websocket):
    while True:
        try:
            data = await websocket.recv()
            text = TextFormat(json.loads(data))
            reply = text.analyse_purpose()
            await websocket.send(reply)
        except websockets.ConnectionClosedOK:
            break

async def websock_server():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(websock_server())
