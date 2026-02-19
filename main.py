from fastapi import FastAPI

app = FastAPI()  # 👈 Yeh zaroori hai

@app.get("/")
def read_root():
    return {"message": "Good work"}

@app.get("/ping")
def ping():
    return {"status": "alive"}
