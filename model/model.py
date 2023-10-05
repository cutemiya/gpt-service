from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    text: str
    datetime: str
    request_text: str


class Answer(BaseModel):
    text: str
    is_right: bool


class Question(BaseModel):
    title: str
    answers: List[Answer]


class Test(BaseModel):
    title: str
    description: str
    questions: List[Question]
