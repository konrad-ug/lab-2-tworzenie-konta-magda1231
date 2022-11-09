import unittest

from ..Konto import Konto

class TestKsięgowanieKonto(unittest.TestCase):
    imie = "Darek"
    nazwisko = "Kowalski"
    pesel = "1111111111"

    def test_nieudany_przelew_wychodzący(self):
       konto = Konto(self.imie,self.nazwisko,self.pesel)
       konto.saldo = 100
       konto.zaksięguj_przelew_wychodzący(800)
       self.assertEqual(konto.saldo, 100)

    def test_ujemny_przelew_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(-800)
        self.assertEqual(konto.saldo, 1000)
    
    def test_udany_przelew_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.saldo, 1000-800)

    def test_udany_przelew_przychodący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(konto.saldo, 1000+800)

    def test_ujemny_przelew_przychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(-800)
        self.assertEqual(konto.saldo, 1000)


    def test_udany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.saldo, 1000-800-1)

    def test_udany_wychodzący_przelew_ekspresowy_konto_ujemne_o_opłatę(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 800
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.saldo, 800-800-1)

    def test_nieudany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.saldo,700)

    def test_ujemny_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(-800)
        self.assertEqual(konto.saldo,700)

