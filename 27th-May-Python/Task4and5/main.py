from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx
import json
import asyncio

app = FastAPI()

API_KEY = "AIzaSyBg0E-0EBidTsNZ0hlMT-O7pq6Ka_aDYMI"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key={API_KEY}"


async def stream_gemini(prompt: str):

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    async with httpx.AsyncClient(timeout=None, verify=False) as client:
        async with client.stream("POST", URL, json=payload) as response:

            async for line in response.aiter_lines():

                if line:
                    try:
                        data = json.loads(line)

                        text = (
                            data.get("candidates", [{}])[0]
                            .get("content", {})
                            .get("parts", [{}])[0]
                            .get("text", "")
                        )

                        if text:
                            yield json.dumps({"chunk": text}) + "\n"

                    except:
                        continue


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")

    return StreamingResponse(
        stream_gemini(prompt),
        media_type="text/plain"
    )