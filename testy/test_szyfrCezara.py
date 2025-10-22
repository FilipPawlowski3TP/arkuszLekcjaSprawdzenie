from konsolowa import konsolowka
import unittest

from konsolowa.konsolowka import szyfruj


class SzyfrCezaraTest(unittest.TestCase):
    def test_klucz_dodatki(self):
        self.assertEqual(szyfruj("abc",3),"def")
    def test_zawijanie(self):
        self.assertEqual(szyfruj("xyz",3),"abc")
    def test_klucz_ujemny(self):
        self.assertEqual(szyfruj("def",-3),"abc")
    def test_duzy_klucz(self):
        self.assertEqual(szyfruj("abc",29),"def")
    def test_spacja(self):
        self.assertEqual(szyfruj("ab cd",2),"cd ef")