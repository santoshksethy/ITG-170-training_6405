from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
import httpx
import json
import os
load_dotenv()
app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"


async def stream_llama(prompt: str):

    if not GROQ_API_KEY:
        yield json.dumps({"error": "Missing GROQ_API_KEY"}) + "\n"
        return

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", URL, json=payload, headers=headers) as response:

            async for line in response.aiter_lines():

                if not line:
                    continue

                # Groq sends: data: {...}
                if line.startswith("data: "):
                    line = line.replace("data: ", "")

                if line == "[DONE]":
                    break

                try:
                    data = json.loads(line)

                    content = (
                        data.get("choices", [{}])[0]
                        .get("delta", {})
                        .get("content")
                    )

                    if content:
                        yield json.dumps({"chunk": content}) + "\n"

                except Exception:
                    continue


@app.api_route("/chat", methods=["GET", "POST"])
async def chat(request: Request):

    prompt = ""

    # 1️⃣ GET query param support
    if request.method == "GET":
        prompt = request.query_params.get("prompt", "")

    # 2️⃣ POST JSON body support
    else:
        body = await request.json()
        prompt = body.get("prompt", "")

    return StreamingResponse(
        stream_llama(prompt),
        media_type="text/plain"
    )