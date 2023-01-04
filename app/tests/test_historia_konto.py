import unittest

from ..Account import Account

class TestHistoriaAccount(unittest.TestCase):
    name = "Ala"
    surname = "Kota"
    pesel = "11111111111"
    
    def test_history_udany_przelew_wychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(account.history,[-800])

    def test_history_udany_przelew_przychodący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(account.history,[800])

    def test_history_ujemny_przelew_przychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_przychodzący(-800)
        self.assertEqual(account.history, [])

    def test_history_ujemny_przelew_wychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_przelew_wychodzący(-800)
        self.assertEqual(account.history, [])

    def test_history_udany_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 1000
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.history, [-800,-1])

    def test_history_nieudany_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 700
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.history,[])

    def test_history_ujemny_wychodzący_przelew_ekspresowy(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 700
        account.zaksięguj_wychodzacy_przelew_ekspresowy(-800)
        self.assertEqual(account.history,[])

    def test_history_przelew_przychodzący_wychodzący(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 700
        account.zaksięguj_przelew_przychodzący(800)
        account.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(account.history,[800,-800])
    
    def test_history_pare_przelewów(self):
        account = Account(self.name,self.surname,self.pesel)
        account.balance = 10000
        account.zaksięguj_przelew_wychodzący(500)
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        account.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(account.history, [-500, -800, -1, -700, -1]) 
