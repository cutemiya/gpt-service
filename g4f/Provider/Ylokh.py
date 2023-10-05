from __future__ import annotations

import json

from ..requests import StreamSession
from .base_provider import AsyncGeneratorProvider
from ..typing import AsyncGenerator

class Ylokh(AsyncGeneratorProvider):
    url                   = "https://chat.ylokh.xyz"
    working               = True
    supports_gpt_35_turbo = True


    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: list[dict[str, str]],
        stream: bool = True,
        proxy: str = None,
        **kwargs
    ) -> AsyncGenerator:
        model = model if model else "gpt-3.5-turbo"
        headers = {
            "Origin"             : cls.url,
            "Referer"            : cls.url + "/",
        }
        data = {
            "messages": messages,
            "model": model,
            "temperature": 1,
            "presence_penalty": 0,
            "top_p": 1,
            "frequency_penalty": 0,
            "allow_fallback": True,
            "stream": stream,
            **kwargs
        }
        async with StreamSession(
            headers=headers,
            proxies={"https": proxy}
        ) as session:
            async with session.post("https://chatapi.ylokh.xyz/v1/chat/completions", json=data) as response:
                response.raise_for_status()
                if stream:
                    async for line in response.iter_lines():
                        line = line.decode()
                        if line.startswith("data: "):
                            if line.startswith("data: [DONE]"):
                                break
                            line = json.loads(line[6:])
                            content = line["choices"][0]["delta"].get("content")
                            if content:
                                yield content
                else:
                    chat = await response.json()
                    yield chat["choices"][0]["message"].get("content")



    @classmethod
    @property
    def params(cls):
        params = [
            ("model", "str"),
            ("messages", "list[dict[str, str]]"),
            ("stream", "bool"),
            ("proxy", "str"),
            ("temperature", "float"),
            ("top_p", "float"),
        ]
        param = ", ".join([": ".join(p) for p in params])
        return f"g4f.provider.{cls.__name__} supports: ({param})"