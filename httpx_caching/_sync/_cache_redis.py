from typing import Optional, Tuple

import redis

from httpx_caching._models import Response
from httpx_caching._serializer import Serializer


class SyncRedisCache:
    def __init__(
        self,
        cache: redis.Redis,
        serializer: Optional[Serializer] = None,
    ) -> None:
        self.serializer = serializer if serializer else Serializer()
        self.redis = cache

    def get(self, key: str) -> Tuple[Optional[Response], Optional[dict]]:
        value = self.redis.get(key)
        return self.serializer.loads(value)

    def set(
        self, key: str, response: Response, vary_header_data: dict, response_body: bytes
    ) -> None:
        self.redis.set(
            key, self.serializer.dumps(response, vary_header_data, response_body)
        )

    def delete(self, key: str) -> None:
        self.redis.delete(key)

    def close(self):
        pass
