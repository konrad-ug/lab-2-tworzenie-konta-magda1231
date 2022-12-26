import unittest

from ..Account import Account

class TestKsięgowanieAccount(unittest.TestCase):
    name = "Darek"
    surname = "Kowalski"
    pesel = "1111111111"

    def test_nieudany_przelew_wychodzący(self):
       account = Account(self.name,self.surname,self.pesel)
       account.balance = 100
       account.zaksięguj_przelew_wychodzący(800)
       self.assertEqual(account.balance, 100)

    def test_ujemny_przelew_wychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_wychodzący(-800)
        self.assertEqual(account.balance, 1000)
    
    def test_udany_przelew_wychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(account.balance, 1000-800)

    def test_udany_przelew_przychodący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(account.balance, 1000+800)

    def test_ujemny_przelew_przychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_przychodzący(-800)
        self.assertEqual(account.balance, 1000)


    def test_udany_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.balance, 1000-800-1)

    def test_udany_wychodzący_przelew_ekspresowy_account_ujemne_o_opłatę(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 800
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.balance, 800-800-1)

    def test_nieudany_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 700
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.balance,700)

    def test_ujemny_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 700
        account.zaksięguj_wychodzacy_przelew_ekspresowy(-800)
        self.assertEqual(account.balance,700)

