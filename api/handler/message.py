import datetime

from fastapi import APIRouter
from pydantic import BaseModel

import model.model
import service.message
from service.message import GptService

message_router = APIRouter()


@message_router.get("/{req_text}")
def message_get(req_text: str):
    return model.model.Message(
        text=GptService.generate_message(req_text),
        datetime=datetime.datetime.now().__str__(),
        request_text=req_text
    )


class TestRequest(BaseModel):
    title: str
    diff: int


@message_router.post("/test")
def test_get(req: TestRequest) -> model.model.Test:
    return service.message.GptService.generate_test(req.title, "")


@message_router.post("/question")
def gen_question(req: TestRequest) -> model.model.Question:
    return service.message.GptService.generate_question(req.title, req.diff)
