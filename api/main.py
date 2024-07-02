from fastapi import fastAPI

app = FastAPI()

@app.get("/")
async def health_checck():
    return "The health check is succesful!"