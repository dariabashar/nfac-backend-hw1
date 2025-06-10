#точка входа
from fastapi import FastAPI
from . import models
from src import database
from src.api import router as api_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

