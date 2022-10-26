import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self): 
        pesel = "11111111111"
        saldo = "50zł"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel , "Niepoprawny pesel")


    def test_zbyt_dlugi_pesel(self): 
        pesel = "1111111111111"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt długiego peselu")

    def test_zbyt_krotki_pesel(self): 
        pesel = "11111"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt krótkiego peselu")

    def test_zbyt_długi_kod(self):
        kod = "PROM_1231223"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "1111111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zbyt długi kod zaakceptowany" )

    def test_zbyt_krótki_kod(self): 
        kod = "PROM_12"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "1111111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zbyt długi kod zaakceptowany" )

    def test_zły_kod(self):
        kod = "KOD_PROMOCYJNY"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "1111111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zły kod zaakceptowany" )

    def test_zły_kod_małe_litery(self):
        kod = "prom_213"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "1111111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zły kod zaakceptowany" )

    def test_saldo_z_dobrym_kodem(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "1111111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Zła ilość pieniędzy" )

    def test_kod_po_1960(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "6511111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Zła ilość pieniędzy" )

    def test_kod_przed_1960(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "6011111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zła ilość pieniędzy" )

