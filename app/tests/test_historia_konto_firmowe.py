import unittest

from ..Company_Account import CompanyAccount

class TestHistoriaCompanyAccount(unittest.TestCase):
    company_name = "ala sp. zoo"
    nip = "1234567890"

    def test_history_księgowanie_udany_przelew_wychodzący_sprawdz(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 1000
        account.zaksięguj_przelew_wychodzący(800)
        self.assertEqual(account.history,[-800])

    def test_history_księgowanie_udany_przelew_przychodący_sprawdz(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 1000
        account.zaksięguj_przelew_przychodzący(800)
        self.assertEqual(account.history,[800])

    def test_history_księgowanie_udany_przelew_expresowy_sprawdz(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 1000
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.history,[-800, -5])

    def test_history_pare_przelewów(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 10000
        account.zaksięguj_przelew_wychodzący(500)
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        account.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(account.history, [-500, -800, -5, -700, -5]) 

   
   


 



    



