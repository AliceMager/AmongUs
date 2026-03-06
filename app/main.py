import uvicorn
from fastapi import FastAPI
from app.routers import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
