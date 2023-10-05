from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.server import main_router


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api/v1")
