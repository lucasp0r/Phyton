import unittest
from unittest.case import TestCase
from os import path

PROJECT_PATH = path.dirname(__file__)
PROJECT_PATH = path.abspath(path.join(PROJECT_PATH, '..'))

import sys

sys.path.append(PROJECT_PATH)

from githubxml.operacao import soma


class SomaTests(TestCase):
    def test_1_mais_1(self):
        resultado = soma(1, 1)
        self.assertEqual(2, resultado)

    def test_2_mais_2(self):
        self.assertEqual(4, soma(2, 2))

    def test_float(self):
        self.assertEqual(2.3, soma(1.1, 1.2))




if __name__ == "__main__":
    unittest.main()
