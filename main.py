"""Application Entrypoint"""
import asyncio
import traceback

import httpx
import websockets
from fastapi import FastAPI, HTTPException, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect

## Modules
from pages.home import html_template
from src.config import API_KEY, API_URL, API_WS_URL
from src.models.req_body import RequestBodyContextChat
from src.models.res_body import ResponseBodyContextChat

app = FastAPI(
    title='Prompt Engineers Proxy API', 
    version='v0.0.1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###############################################
##  Pages
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
##  Routes
###############################################
@app.post(
    "/api/proxy",
    response_model=ResponseBodyContextChat,
    tags=["Chat - WebSocket Stream"],
    # description=CHAT_VECTORSTORE_SOCKET_MESSAGE_DESCRIPTION
)
async def send_message_to_context_chat_socket(
    request: Request,
    body: RequestBodyContextChat,
    channel: str or None = None
):
    # URL of the external API endpoint
    url = f'{API_URL}/api/v1/chat/vectorstore/message?channel={channel}'
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    data = body.dict()  # Convert the body to a dict, which will be converted to JSON
    
    timeout = httpx.Timeout(30.0, read=120.0)  # Increase the timeout to 10 seconds for connect and 30 seconds for read

    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(url, json=data, headers=headers)

    print(url)
    print(response.content)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send message to context chat")
    
    # return response.json()
    return {
        "status": "success", 
        "channel": channel,
        "message": "Message successfully sent!"
    }

###############################################
##  Sockets
###############################################
@app.websocket("/ws/proxy")
async def websocket_proxy_endpoint(
    websocket: WebSocket,
    session: str or None = None,
):
    await websocket.accept()

    async with websockets.connect(f'{API_WS_URL}&session={session}', timeout=120.0) as target_socket:
        async def forward_to_target():
            try:
                while True:
                    try:
                        message = await websocket.receive_text()
                        # print("Forwarding message:", message)
                        await target_socket.send(message)
                    except WebSocketDisconnect:
                        print("Target disconnected")
                        await target_socket.close() 
                        break
            except Exception as e:
                print(f"Error forwarding messages to target: {e}")

        async def forward_to_client():
            try:
                while True:
                    try:
                        message = await target_socket.recv()
                        # print("Forwarding message:", message)
                        await websocket.send_text(message)
                    except WebSocketDisconnect:
                        print("Client disconnected")
                        await websocket.close() 
                        break
            except Exception as e:
                print(f"Error forwarding messages to client: {e}")

        await asyncio.gather(forward_to_target(), forward_to_client())