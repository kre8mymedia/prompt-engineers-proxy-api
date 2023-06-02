"""Application Entrypoint"""
import asyncio
import websockets
from fastapi import FastAPI, WebSocket
from starlette.responses import HTMLResponse

## Modules
from pages.home import html_template
from src.config import API_KEY, API_URL, API_WS_URL, S3_BUCKET

app = FastAPI()

###############################################
##  Routes
###############################################
@app.get(
    "/", 
    response_class=HTMLResponse,
    tags=["Pages"],
    include_in_schema=False
)
async def get_root():
    """Default Home Page"""
    return html_template

###############################################
##  Sockets
###############################################
@app.websocket("/ws-proxy")
async def websocket_proxy_endpoint(websocket: WebSocket):
    await websocket.accept()

    async with websockets.connect(API_WS_URL) as target_socket:
        async def forward_to_target():
            try:
                while True:
                    message = await websocket.receive_text()
                    print("Forwarding message:", message)
                    await target_socket.send(message)
            except Exception as e:
                print(f"Error forwarding messages to target: {e}")

        async def forward_to_client():
            try:
                while True:
                    message = await target_socket.recv()
                    print("Forwarding message:", message)
                    await websocket.send_text(message)
            except Exception as e:
                print(f"Error forwarding messages to client: {e}")

        await asyncio.gather(forward_to_target(), forward_to_client())
        
###############################################
##  Sockets
###############################################
@app.websocket("/formio-proxy")
async def websocket_proxy_endpoint(websocket: WebSocket):
    await websocket.accept()

    async with websockets.connect(f"wss://{API_URL}/chat-vector-db?api_key={API_KEY}&bucket={S3_BUCKET}&path=formio.pkl") as target_socket:
        async def forward_to_target():
            try:
                while True:
                    message = await websocket.receive_text()
                    print("Forwarding message:", message)
                    await target_socket.send(message)
            except Exception as e:
                print(f"Error forwarding messages to target: {e}")

        async def forward_to_client():
            try:
                while True:
                    message = await target_socket.recv()
                    print("Forwarding message:", message)
                    await websocket.send_text(message)
            except Exception as e:
                print(f"Error forwarding messages to client: {e}")

        await asyncio.gather(forward_to_target(), forward_to_client())
        
###############################################
##  Sockets
###############################################
@app.websocket("/miele-proxy")
async def websocket_proxy_endpoint(websocket: WebSocket):
    await websocket.accept()

    async with websockets.connect(f"wss://{API_URL}/chat-vector-db?api_key={API_KEY}&bucket={S3_BUCKET}&path=miele-vectorstore.pkl") as target_socket:
        async def forward_to_target():
            try:
                while True:
                    message = await websocket.receive_text()
                    print("Forwarding message:", message)
                    await target_socket.send(message)
            except Exception as e:
                print(f"Error forwarding messages to target: {e}")

        async def forward_to_client():
            try:
                while True:
                    message = await target_socket.recv()
                    print("Forwarding message:", message)
                    await websocket.send_text(message)
            except Exception as e:
                print(f"Error forwarding messages to client: {e}")

        await asyncio.gather(forward_to_target(), forward_to_client())