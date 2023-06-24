import os

WS_URL = os.environ["WS_URL"]
API_URL = os.environ["API_URL"]
API_KEY = os.environ["API_KEY"]
S3_BUCKET = os.environ["S3_BUCKET"]
VECTORSTORE = os.environ["VECTORSTORE"]

API_WS_URL = f"{WS_URL}/ws/v1/chat/vectorstore?api_key={API_KEY}&bucket={S3_BUCKET}&path={VECTORSTORE}"