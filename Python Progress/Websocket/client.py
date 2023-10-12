import asyncio
import websockets


async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Enter a message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response from server: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
