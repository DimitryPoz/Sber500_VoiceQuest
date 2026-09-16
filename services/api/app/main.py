from fastapi import FastAPI

app = FastAPI(
    title="VoiceQuest API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/scenes")
def scenes():
    return {
        "items": [],
        "message": "Scene service is ready for MVP implementation.",
    }
