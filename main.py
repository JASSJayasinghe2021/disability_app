from fastapi import FastAPI

app = FastAPI()

@app.get("/consent")
async def root():
    return {"message":"Hi"}

@app.get("/districts")
async def root():
    return {
            "districts":["Colombo", "Badulla"],
        }
    

@app.get("/ds")
async def root():
    return {
            "ds":["Badulla", "Passara"],
        }

@app.get("/gn")
async def root():
    return {
            "gs":["Badulla South", "Badulla North"],
        }