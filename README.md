<p align="center">Caching for HTTPX.</em></p>

<p align="center">
<a href="https://github.com/johtso/httpx-caching/actions">
    <img src="https://github.com/johtso/httpx-caching/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
</p>

**Note**: Early development / alpha, use at your own risk.

This package adds caching functionality to [HTTPX](https://github.com/encode/httpx)

Adapted from Eric Larson's fantastic [CacheControl](https://github.com/ionrock/cachecontrol) for [requests](https://requests.readthedocs.io/en/stable/).

Project goals:
* Sans-io caching protocol
* Support multiple http clients (currently only supports httpx)
* Fully async compatible

Limitations:
* Currently only has in-memory cache storage

**Usage:**

```python
from httpx import AsyncClient
from httpx_caching import CachingClient

client = AsyncClient()
client = CachingClient(client)

async client.get("http://example.com")
```


**Documentation:**

TODO

See [CacheControl's documentation](https://cachecontrol.readthedocs.io/en/latest/index.html) for general documentation of the caching approach.
