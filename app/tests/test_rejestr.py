import unittest

from ..RejestrKont import RejestrKont
from .. Konto import Konto

class TestRejestrKont(unittest.TestCase):
    imie = "Darek"
    imie2 = "Darek"
    nazwisko = "Kowalski"
    nazwisko2 = "Kowalski"
    pesel = "11111111111"
    pesel2 = "11111111111"

    @classmethod
    def SetUpClass(cls):
        cls.konto = Konto(cls.imie,cls.nazwisko,cls.pesel)
        RejestrKont.dodaj_konto(cls.konto)

    def test_0_ile_kont(self):
        RejestrKont.ile_kont()
        self.assertEqual(RejestrKont.ile_kont(),1)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []

    def test_1_dodaj_konto(self):
        self.assertEqual(RejestrKont.ile_kont(),0)

   
    def test_1_dodaj_konto(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(),1)

    def test_2_dodaj_2_konta(self):
        konto2 = Konto(self.imie,self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto2)
        self.assertEqual(RejestrKont.ile_kont(),2)

    def test_3_ile_kont(self):
        RejestrKont.ile_kont()
        self.assertEqual(RejestrKont.ile_kont(),2)

    def test_4_znajdz_po_peselu(self):
        konto = Konto(self.imie,self.nazwisko,"21111111111")
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.znajdz_konto("21111111111"),konto)

    def test_5_znajdz_po_peselu_zły_pesel(self):
        self.assertEqual(RejestrKont.znajdz_konto("111111111"),"To jest zły pesel")




