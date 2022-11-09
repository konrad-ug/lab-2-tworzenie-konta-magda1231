import unittest

from ..Konto_firmowe import KontoFirmowe

class TestKsięgowanieKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "company sp.zoo"
    nip = "1111111111"

    def test_działający_przelew_wychodzący(self):
        account = KontoFirmowe(self.nazwa_firmy,self.nip)
        account.saldo = 800
        account.zaksięguj_przelew_wychodzący(700)
        self.assertEqual(account.saldo, 800-700)

    def test_działający_przelew_przychodzący(self):
        account = KontoFirmowe(self.nazwa_firmy,self.nip)
        account.saldo = 800
        account.zaksięguj_przelew_przychodzący(700)
        self.assertEqual(account.saldo, 800+700)

    def test_udany_wychodzący_przelew_ekspresow_firmowe(self):
        account = KontoFirmowe(self.nazwa_firmy,self.nip)
        account.saldo = 800
        account.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(account.saldo, 800-700-5)

    def test_udany_wychodzący_przelew_ekspresowy_konto_ujemne_o_opłatę(self):
        account = KontoFirmowe(self.nazwa_firmy,self.nip)
        account.saldo = 800
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.saldo, 800-800-5)

    def test_nieudany_wychodzący_przelew_ekspresowy(self):
        account = KontoFirmowe(self.nazwa_firmy,self.nip)
        account.saldo = 100
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.saldo,100)



