import unittest

from ..Konto import Konto


class TestHistoria(unittest.TestCase):
    imie = "Ala"
    nazwisko = "Kota"
    pesel = "11111111111"
    nazwa_firmy = "ala sp. zoo"
    nip = "1234567890"
    
    def test_księgowanie_udany_przelew_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.historia,[-800])

    def test_księgowanie_udany_przelew_przychodący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(konto.historia,[800])

    def test_księgowanie_ujemny_przelew_przychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(-800)
        self.assertEqual(konto.historia, [])

    def test_księgowanie_udany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia, [-800,-1])

    def test_księgowanie_nieudany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia,[])

    def test_księgowanie_ujemny_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(-800)
        self.assertEqual(konto.historia,[])

    def test_księgowanie_przelew_przychodzący_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_przelew_przychodzący(800)
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.historia,[800,-800])

    
    def test_udany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 10000
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia, [-800,-1, -700, -1]) 
