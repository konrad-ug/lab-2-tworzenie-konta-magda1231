import unittest


from ..Konto_firmowe import KontoFirmowe

class TestHistoriaKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "ala sp. zoo"
    nip = "1234567890"

    def test_historia_księgowanie_udany_przelew_wychodzący_sprawdz(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 1000
        konto.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(konto.historia,[-800])

    def test_historia_księgowanie_udany_przelew_przychodący_sprawdz(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 1000
        konto.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(konto.historia,[800])

    def test_historia_księgowanie_udany_przelew_expresowy_sprawdz(self):
        konto = KontoFirmowe(self.nazwa_firmy,self.nip)
        konto.saldo = 1000
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia,[-800, -5])

    def test_historia_pare_przelewów(self):
        konto = KontoFirmowe(self.imie,self.nazwisko,self.pesel)
        konto.saldo = 10000
        konto.zaksięguj_przelew_przychodzący(500)
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        konto.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(konto.historia, [500, -800, -5, -700, -5]) 

   
   


 



    



