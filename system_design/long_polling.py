import asyncio
from aiohttp import web
import uuid

# Event storage
class MessageManager:
    def __init__(self):
        self.messages = {}
        self.waiting_clients = {}
    
    async def wait_for_message(self, client_id, last_message_id=None):
        # Create future for this client
        if client_id not in self.waiting_clients:
            self.waiting_clients[client_id] = []
        
        # Create a future that will be resolved when a message arrives
        future = asyncio.Future()
        self.waiting_clients[client_id].append(future)
        
        try:
            # Wait for the future to be resolved
            return await asyncio.wait_for(future, timeout=30.0)
        except asyncio.TimeoutError:
            # Remove this future from waiting list
            if client_id in self.waiting_clients and future in self.waiting_clients[client_id]:
                self.waiting_clients[client_id].remove(future)
            return None
    
    async def send_message(self, message, target_client=None):
        message_id = str(uuid.uuid4())
        self.messages[message_id] = message
        
        # Notify waiting clients
        if target_client and target_client in self.waiting_clients:
            for future in self.waiting_clients[target_client]:
                if not future.done():
                    future.set_result((message_id, message))
            self.waiting_clients[target_client] = []
        elif target_client is None:
            # Broadcast to all waiting clients
            for client_id, futures in list(self.waiting_clients.items()):
                for future in futures:
                    if not future.done():
                        future.set_result((message_id, message))
                self.waiting_clients[client_id] = []
        
        return message_id

# Create the application
app = web.Application()
manager = MessageManager()

async def poll_handler(request):
    client_id = request.match_info.get('client_id')
    last_message_id = request.query.get('last', None)
    
    result = await manager.wait_for_message(client_id, last_message_id)
    
    if result is None:
        return web.json_response({"status": "timeout", "message": None})
    else:
        message_id, message = result
        return web.json_response({
            "status": "message",
            "message_id": message_id,
            "message": message
        })

async def send_handler(request):
    data = await request.json()
    message = data.get('message')
    target_client = data.get('client_id', None)
    
    message_id = await manager.send_message(message, target_client)
    
    return web.json_response({
        "status": "sent",
        "message_id": message_id
    })

# Setup routes
app.router.add_get('/poll/{client_id}', poll_handler)
app.router.add_post('/send', send_handler)

if __name__ == '__main__':
    web.run_app(app)