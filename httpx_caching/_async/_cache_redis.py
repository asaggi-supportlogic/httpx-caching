from typing import Optional, Tuple

import redis.asyncio as redis

from httpx_caching._models import Response
from httpx_caching._serializer import Serializer


class AsyncRedisCache:
    def __init__(
        self,
        cache: redis.Redis,
        serializer: Optional[Serializer] = None,
    ) -> None:
        self.serializer = serializer if serializer else Serializer()
        self.redis = cache

    async def aget(self, key: str) -> Tuple[Optional[Response], Optional[dict]]:
        value = await self.redis.get(key)
        return self.serializer.loads(value)

    async def aset(
        self, key: str, response: Response, vary_header_data: dict, response_body: bytes
    ) -> None:
        await self.redis.set(
            key, self.serializer.dumps(response, vary_header_data, response_body)
        )

    async def adelete(self, key: str) -> None:
        await self.redis.delete(key)

    async def aclose(self):
        pass
