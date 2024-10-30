from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/", response_model=dict)
async def root() -> JSONResponse:
    return JSONResponse(content={"message": "Hello World"})
