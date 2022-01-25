import websockets

import messages as msg

class Clients:
    clients = set()
    
    def __init__(self) -> None:
        pass

    async def new(self, ws):
        # Each time a new client connect
        print(f'A client just connected {ws.remote_address}')
        self.clients.add(ws)

    async def send(self, msg: str, client = None):
        """Send message to clients/client
        Args:
            msg (str): message to send
            client (WebSocketServerProtocol, optional): the client receive message. Defaults to None (send to all clients).
        """
        if client:
            await client.send(msg)
        else:
            for c in self.clients:
                await c.send(msg)


    async def receiveMsgs(self, ws):
        """Listen to the port and receive messages from client
        Args:
            ws (WebSocketServerProtocol): websocket connection
        """
        try:
            # Welcome message
            await ws.send("Server is connected")

            # Wait for client sending messages
            while True:
                message = await ws.recv()
                await msg.decoding(ws, message)

        except websockets.exceptions.ConnectionClosed as e:
            print(f'A client just disconnected {ws.remote_address}')
            # print(e)

        finally:
            self.clients.remove(ws)


    