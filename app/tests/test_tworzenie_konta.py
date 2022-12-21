import unittest

from ..Account import Account

class TestTworzenieaccounts(unittest.TestCase):

    def test_tworzenie_accounts(self): 
        pesel = "11111111111"
        balance = "50zł"
        first_account = Account("Dariusz", "Januszewski", pesel)
        self.assertEqual(first_account.name, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(first_account.surname, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(first_account.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(first_account.pesel, pesel , "Niepoprawny pesel")
        self.assertEqual(first_account.history, [] , "Zła początkowa history")


    def test_zbyt_dlugi_pesel(self): 
        pesel = "6111111111111"
        first_account = Account("Dariusz", "Januszewski", pesel)
        self.assertEqual(first_account.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt długiego peselu")

    def test_zbyt_krotki_pesel(self): 
        pesel = "61111"
        first_account = Account("Dariusz", "Januszewski", pesel)
        self.assertEqual(first_account.pesel, "Niepoprawny pesel", "Zła wartość wyświetlana w przypadku zbyt krótkiego peselu")

    def test_zbyt_długi_kod_po_1960(self):
        kod = "PROM_1231223"
        first_account = Account("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(first_account.balance, 0, "Zbyt długi kod zaakceptowany" )

    def test_zbyt_krótki_kod_po_1960(self): 
        kod = "PROM_12"
        first_account = Account("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(first_account.balance, 0, "Zbyt długi kod zaakceptowany" )

    def test_zły_kod_po_1960(self):
        kod = "KOD_PROMOCYJNY"
        first_account = Account("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(first_account.balance, 0, "Zły kod zaakceptowany" )

    def test_zły_kod_małe_litery_po_1960(self):
        kod = "prom_213"
        first_account = Account("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(first_account.balance, 0, "Zły kod zaakceptowany" )

    def test_balance_z_dobrym_kodem_po_1960(self):
        kod = "PROM_3.1"
        first_account = Account("Dariusz", "Januszewski", "61111111111", kod)
        self.assertEqual(first_account.balance, 50, "Zła ilość pieniędzy" )

    def test_dobry_kod_przed_1960(self):
        kod = "PROM_3.1"
        first_account = Account("Dariusz", "Januszewski", "50111111111", kod)
        self.assertEqual(first_account.balance, 0, "Kod przyznany osobie urodzonej przed 1960" )

    def test_dobry_kod_w_1960(self):
        kod = "PROM_3.1"
        first_account = Account("Dariusz", "Januszewski", "60111111111", kod)
        self.assertEqual(first_account.balance, 0, "Kod przyznany osobie urodzonej w 1960" )

    def test_dobry_kod_przed_1900(self):
        kod = "PROM_3.1"
        first_account = Account("Dariusz", "Januszewski", "98811111111", kod)
        self.assertEqual(first_account.balance, 0, "Kod przyznany osobie urodzonej przed 1960" )

    def test_dobry_kod_po_2000(self):
        kod = "PROM_3.1"
        first_account = Account("Dariusz", "Januszewski", "21211111111", kod)
        self.assertEqual(first_account.balance, 50, "Kod nieprzyznany osobie urodzonej po 2000" )