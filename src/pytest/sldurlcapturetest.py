import unittest
from UrlCapture import Url


class CaptureTest(unittest.TestCase):

    def test_urlcapture(self):
        self.assertEqual("http://somewhat.com/url", Url.urlcapture("Hi http://somewhat.com/url/ "))
        self.assertEqual("http://somewhat.com/url", Url.urlcapture("http://somewhat.com/url world"))
        self.assertEqual("http://somewhat.com/url", Url.urlcapture("Hi http://somewhat.com/url world"))
