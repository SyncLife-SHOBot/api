from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.api.v1.user.infrastructure.routes import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/", response_model=dict)
async def root() -> JSONResponse:
    return JSONResponse(content={"message": "Hello World"})
