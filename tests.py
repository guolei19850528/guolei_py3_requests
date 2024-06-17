import unittest

from addict import Dict
from requests import Response

from guolei_py3_requests import requests_request


class RequestsTestCase(unittest.TestCase):
    def test_requests_request_001(self):
        def requests_response_callble(response: Response = None):
            if isinstance(response, Response) and response.status_code == 200:
                return response.text
            return None

        response = requests_request(
            requests_response_callable=requests_response_callble,
            requests_request_kwargs={
                "url": "https://www.baidu.com",
                "method": "GET"
            }
        )
        print(response)
        self.assertTrue(True, "OK")  # add assertion here


if __name__ == '__main__':
    unittest.main()
