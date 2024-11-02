from fastapi import FastAPI

app = FastAPI()

@app.get("/consent")
async def root():
    return {"message":""}