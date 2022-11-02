import unittest

from ..Konto_firmowe import KontoFirmowe

class TestKsięgowanie(unittest.TestCase):
    nazwa_firmy = "company sp.zoo"
    nip = "1111111111"

    def test_działający_przelew_wychodzący(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 800
        konto.zaksięguj_przelew_wychodzący(700)
        self.assertEqual(konto.saldo, 800-700)

    def test_działający_przelew_przychodzący(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 800
        konto.zaksięguj_przelew_przychodzący(700)
        self.assertEqual(konto.saldo, 800+700)

    def test_udany_wychodzący_przelew_ekspresow_firmowe(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 800
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(konto.saldo, 800-700-5)

    def test_udany_wychodzący_przelew_ekspresowy_konto_ujemne_o_opłatę(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 800
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.saldo, 800-800-5)


    def test_nieudany_wychodzący_przelew_ekspresowy(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 100
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.saldo,100)



