import unittest
from Pangramcode import *


class Testpangram(unittest.TestCase):

    def test_pangram1(self):                                            # тест для перевірки неправильності функції
        self.assertEqual(pangram("ff"), False)

    def test_pangram2(self):                                            # тест для перевірки правильності функції
        self.assertEqual(pangram("The quick brown fox jumps over the lazy dog."), True)


if __name__ == '__main__':
    unittest.main()
