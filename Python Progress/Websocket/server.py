import asyncio
import websockets


# Function to handle incoming WebSocket connections
async def handle_connection(websocket, path):
    async for message in websocket:
        # When the server receives a message, print it
        print(f"Received message: {message}")

        # Send a response back to the client
        response = f"Server received: {message}"
        await websocket.send(response)

# Create and run the WebSocket server
start_server = websockets.serve(handle_connection, "localhost", 8765)

# Start the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
