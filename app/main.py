from fastapi import FastAPI

app = FastAPI(
    title="Research Agent API",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "Research Agent Running 🚀"
    }