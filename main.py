from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/test")
def basic_print():
    return {"msg": "Hello from test"}

@app.get("/test/{nam}")
def get_name_and_save(name: str):
    file = "names.txt"
    with open(file, "a") as f:
       f.write(name+"\n")
    return {"msg": "saved user"}




