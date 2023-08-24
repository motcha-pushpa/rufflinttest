from fastapi import FastAPI
app = FastAPI()

# test message 23
@app.get("/")
async def root():
    
    return {"message": "hello"}

