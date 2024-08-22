from fastapi import Depends, FastAPI

from app.routers import ping

app = FastAPI()

app.include_router(ping.router)


@app.get("/")
async def root():
    return {"message": "OK"}

@app.get("/health")
async def health():
    return {"message": "OK"}