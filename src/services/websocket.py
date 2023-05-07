from fastapi import WebSocket

async def forward(src: WebSocket, dst: WebSocket):
    """Forwards to source websocket"""
    try:
        while True:
            message = await src.receive_text()
            print("Forwarding message:", message)
            await dst.send_text(message)
    except Exception as e:
        print(f"Error forwarding messages: {e}")