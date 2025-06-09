import asyncio
import websockets

async def handler(websocket, path):
    print("New client connected!")
    await websocket.send("Welcome! Your WebSocket is live.")
    while True:
        try:
            message = await websocket.recv()
            print("Received:", message)
            await websocket.send(f"Echo: {message}")
        except:
            print("Client disconnected")
            break

start_server = websockets.serve(handler, "0.0.0.0", 8000)

print("WebSocket server starting at ws://localhost:8000...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
