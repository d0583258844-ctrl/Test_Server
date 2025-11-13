from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/test")
def basic_print():
    return {"msg": "Hello from test"}




