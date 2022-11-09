import unittest

from ..Konto import Konto

class TestHistoriaKonto(unittest.TestCase):
    imie = "Ala"
    nazwisko = "Kota"
    pesel = "11111111111"
    
    def test_historia_udany_przelew_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.historia,[-800])

    def test_historia_udany_przelew_przychodący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(konto.historia,[800])

    def test_historia_ujemny_przelew_przychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(-800)
        self.assertEqual(konto.historia, [])

    def test_historia_ujemny_przelew_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(-800)
        self.assertEqual(konto.historia, [])

    def test_historia_udany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 1000
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia, [-800,-1])

    def test_historia_nieudany_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia,[])

    def test_historia_ujemny_wychodzący_przelew_ekspresowy(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(-800)
        self.assertEqual(konto.historia,[])

    def test_historia_przelew_przychodzący_wychodzący(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 700
        konto.zaksięguj_przelew_przychodzący(800)
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.historia,[800,-800])
    
    def test_historia_pare_przelewów(self):
        konto = Konto(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 10000
        konto.zaksięguj_przelew_wychodzący(500)
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(konto.historia, [-500, -800, -1, -700, -1]) 
