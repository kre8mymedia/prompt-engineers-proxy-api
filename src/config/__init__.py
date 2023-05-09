import os

API_KEY = os.environ["API_KEY"]
API_URL = os.environ["API_URL"]
S3_BUCKET = os.environ["S3_BUCKET"]
VECTORSTORE = os.environ["VECTORSTORE"]

API_WS_URL = f"wss://{API_URL}/chat-vector-db?api_key={API_KEY}&bucket={S3_BUCKET}&path={VECTORSTORE}"