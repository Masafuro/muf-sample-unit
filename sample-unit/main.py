import os
import uuid
import asyncio
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from muf import MUFClient

app = FastAPI()

# テンプレートエンジンの準備（ディレクトリを明示的に指定）
templates = Jinja2Templates(directory="sample-unit/templates")

REDIS_HOST = os.getenv("REDIS_HOST", "muf-redis")
UNIT_NAME = "sample-unit"

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # index.htmlをレンダリングして返します
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/send")
async def send_to_muf(content: str):
    try:
        async with MUFClient(unit_name=UNIT_NAME, host=REDIS_HOST) as client:
            response = await client.request(
                target_unit="echo-service",
                data=content.encode('utf-8'),
                timeout=5.0
            )
            return {
                "unit": UNIT_NAME,
                "response": response.decode('utf-8'),
                "status": "success"
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))