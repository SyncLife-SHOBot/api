from fastapi import FastAPI
from src.api.v1.shared.infrastructure.http.routes import base_router

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()

app.include_router(base_router, prefix="/api")
