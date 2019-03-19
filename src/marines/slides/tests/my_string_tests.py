import unittest

from slides.py.my_string import *


class TestMyString(unittest.TestCase):
    def test_get_all_urls(self):
        self.assertEqual(get_urls(
            "hi this is my site http://myfirst.site in facebook http://facebook.com/me twitter http://twitter/me my youtube: http://youtube/me"),
            ['http://myfirst.site', 'http://facebook.com/me', 'http://twitter/me', 'http://youtube/me'])

    def test_replace_string(self):
        self.assertEqual(replace("hi every bohidy whihats wronghi", "hi", ""), "every body whats wrong")

    def test_(self):
        self.assertEqual(countLetters("ThiS is String with Upper and lower case Letters"),
                         [('a', 2), ('c', 1), ('d', 1), ('e', 5), ('g', 1), ('h', 2), ('i', 4), ('l', 2), ('n', 2),
                          ('o', 1), ('p', 2), ('r', 4), ('s', 5), ('t', 5), ('u', 1), ('w', 2)])
