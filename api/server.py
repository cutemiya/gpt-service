from fastapi import APIRouter

from api.handler.message import message_router
from api.handler.base import base_router

main_router = APIRouter()
main_router.include_router(message_router, prefix="/message", tags=['message'])
main_router.include_router(base_router, tags=['base'])
