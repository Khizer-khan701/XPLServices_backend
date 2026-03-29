from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import query, voice

app = FastAPI(title="XPLServices AI Agent")

# CORS — Frontend se connect hone ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(voice.router, prefix="/api/voice", tags=["Voice"])

@app.get("/")
def root():
    return {"status": "XPLServices AI Agent Running!"}