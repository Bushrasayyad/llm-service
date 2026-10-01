from fastapi import FastAPI, HTTPException
import time, traceback

from app.schemas import PromptRequest, LLMResponse
from app.llm_client import generate

app = FastAPI(title="LLM Service")

@app.post("/generate", response_model=LLMResponse)
async def generate_endpoint(req: PromptRequest):
    t0 = time.time()
    print(f"[{time.strftime('%H:%M:%S')}] Request received: {req.prompt[:50]}")
    try:
        result = await generate(req.prompt)
        print(f"[{time.strftime('%H:%M:%S')}] LLM responded in {time.time()-t0:.1f}s")
        print(f"[{time.strftime('%H:%M:%S')}] LLM response: {result['response']}")   # ← NEW LINE
        return result
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ERROR after {time.time()-t0:.1f}s: {type(e).__name__} - {e}")
        traceback.print_exc()
        raise HTTPException(status_code=502, detail=f"LLM error: {type(e).__name__}: {e}")

@app.get("/health")
async def health():
    return {"status": "ok"}