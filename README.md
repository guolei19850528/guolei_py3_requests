# guolei_py3_requests

## introduce

**guolei python3 requests library**

## software architecture

~python 3.*

## installation tutorial

```shell
pip install guolei_py3_requests
```

## catalog description

### request example
```python
import guolei_py3_requests

guolei_py3_requests.requests_request(
    requests_response_callable=guolei_py3_requests.RequestsResponseCallable.status_code_200_json,
    requests_request_args=(),
    requests_request_kwargs={}
)
```