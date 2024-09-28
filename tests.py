import unittest

from addict import Dict
from requests import Response

from guolei_py3_requests import requests_request
from guolei_py3_requests.library import request


class RequestsTestCase(unittest.TestCase):
    def test_library(self):
        print(request(method="GET",url="https://www.baidu.com"))
        self.assertTrue(True, "ok")  # add assertion here


if __name__ == '__main__':
    unittest.main()
