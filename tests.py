import unittest
from data import *
from rk1.func import func1, func2, func3

class TestFunctions (unittest.TestCase):

    def test_func1(self):
        self.assertEqual(func1(one_to_many), [('FireFox', 25000, 'Russia'), ('MS Edge', 50000, 'Roma')])

    def test_func2(self):
        self.assertEqual(func2(brs,many_to_many),[(225000, 'China', 'Opera'), (25000, 'Russia', 'FireFox'), (167500, 'USA', 'DuckDuckGo'),
         (70000, 'USA', 'Google'), (50000, 'China', 'Yandex'), (251000, 'USA', 'MS Edge')])

    def test_func3(self):
        self.assertEqual(func3(brs,many_to_many),[[(225000, 'China', 'Opera')], [(25000, 'Russia', 'FireFox'), (50000, 'Roma', 'FireFox'), 
        (60000, 'USA', 'FireFox')], [(167500, 'USA', 'DuckDuckGo')], [(70000, 'USA', 'Google')], [(50000, 'China', 'Yandex'), 
        (67500, 'China', 'Yandex')], [(251000, 'USA', 'MS Edge'), (627500, 'China', 'MS Edge')]])


if __name__ == "__main__":
    unittest.main()