# guolei-py3-requests

### a python3 library for requests by guolei

# Example
```python
from guolei_py3_requests.library import (
    request,
    ResponseCallable
)

result = request(
    response_callable=ResponseCallable.text,
    method="GET",
    url="your url"
)
```