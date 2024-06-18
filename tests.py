import unittest

from addict import Dict
from requests import Response

from guolei_py3_requests import requests_request


class RequestsTestCase(unittest.TestCase):
    def test_requests_request_001(self):
        self.assertTrue(True, "ok")  # add assertion here


if __name__ == '__main__':
    unittest.main()
