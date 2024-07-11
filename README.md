## 介绍

**guolei python3 requests library**

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-requests
```

## 目录说明

### request 示例
```python
import guolei_py3_requests

response = guolei_py3_requests.requests_request(
    requests_response_callable=guolei_py3_requests.RequestsResponseCallable.status_code_200_json,
    requests_request_args=(),
    requests_request_kwargs={}
)
```