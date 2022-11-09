import unittest

from ..Konto import Konto

class TestTworzenieKonta(unittest.TestCase):

    def test_tworzenie_konta(self): 
        pesel = "11111111111"
        saldo = "50zł"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, pesel , "Niepoprawny pesel")
        self.assertEqual(pierwsze_konto.historia, [] , "Zła początkowa historia")


    def test_zbyt_dlugi_pesel(self): 
        pesel = "6111111111111"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt długiego peselu")

    def test_zbyt_krotki_pesel(self): 
        pesel = "61111"
        pierwsze_konto = Konto("Dariusz", "Januszewski", pesel)
        self.assertEqual(pierwsze_konto.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt krótkiego peselu")

    def test_zbyt_długi_kod_po_1960(self):
        kod = "PROM_1231223"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zbyt długi kod zaakceptowany" )

    def test_zbyt_krótki_kod_po_1960(self): 
        kod = "PROM_12"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zbyt długi kod zaakceptowany" )

    def test_zły_kod_po_1960(self):
        kod = "KOD_PROMOCYJNY"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zły kod zaakceptowany" )

    def test_zły_kod_małe_litery_po_1960(self):
        kod = "prom_213"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zły kod zaakceptowany" )

    def test_saldo_z_dobrym_kodem_po_1960(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Zła ilość pieniędzy" )

    def test_dobry_kod_przed_1960(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "50111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Kod przyznany osobie urodzonej przed 1960" )

    def test_dobry_kod_w_1960(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "60111111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Kod przyznany osobie urodzonej w 1960" )

    def test_dobry_kod_przed_1900(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "98811111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 0, "Kod przyznany osobie urodzonej przed 1960" )

    def test_dobry_kod_po_2000(self):
        kod = "PROM_3.1"
        pierwsze_konto = Konto("Dariusz", "Januszewski", "21211111111", kod)
        self.assertEqual(pierwsze_konto.saldo, 50, "Kod nieprzyznany osobie urodzonej po 2000" )