import unittest

from slides.py.collections import *


class TestCollections(unittest.TestCase):
    def setUp(self):
        if(isNewDic()):
            ids=[-1,0,1,5,17,69,32,100,99,452]
            names=["maria","juana","juan carlos","oscar mario sanches","ruddy","MariA","Jorge","mimi","meme","oscar","juan","jaime"]
            load_dictionary(ids, names)
            print dic


    def test_find_user_id(self):
        self.assertEqual(find_users_by_first_id_digit(1),[1, 17, 100])


    def test_find_user_name(self):
        self.assertEqual(find_users_by_first_char_name('m'),['maria', 'mimi', 'meme'])