
import asyncio
import websockets

async def handler(websocket, path):
    # Your connection handler code here
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8000):
        print("Server started on port 8000")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
