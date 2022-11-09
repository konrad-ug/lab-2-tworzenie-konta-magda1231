import unittest
from ..Konto_firmowe import KontoFirmowe

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Idk sp. zoo"
    nip = "1234567890"
    def test_tworzenie_konta(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip )
        self.assertEqual(konto.nazwa_firmy,self.nazwa_firmy, "Nazwa firmy nie została napisana")
        self.assertEqual(konto.nip, self.nip, "Nip nie został zapisany")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest 0")
        self.assertEqual(konto.historia, [] , "Zła początkowa historia")

    def test_zbyt_długi_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip + "123" )
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Niepoprawny nip zaaceptowany")

    def test_zbyt_krótki_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "123456" )
        self.assertEqual(konto.nip, "Niepoprawny NIP", "Niepoprawny nip zaaceptowany")


