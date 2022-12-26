import unittest

from ..Company_Account import CompanyAccount

class TestKsięgowanieCompanyAccount(unittest.TestCase):
    company_name = "company sp.zoo"
    nip = "1111111111"

    def test_działający_przelew_wychodzący(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 800
        account.zaksięguj_przelew_wychodzący(700)
        self.assertEqual(account.balance, 800-700)

    def test_działający_przelew_przychodzący(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 800
        account.zaksięguj_przelew_przychodzący(700)
        self.assertEqual(account.balance, 800+700)

    def test_udany_wychodzący_przelew_ekspresow_firmowe(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 800
        account.zaksięguj_wychodzacy_przelew_ekspresowy(700)
        self.assertEqual(account.balance, 800-700-5)

    def test_udany_wychodzący_przelew_ekspresowy_account_ujemne_o_opłatę(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 800
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.balance, 800-800-5)

    def test_nieudany_wychodzący_przelew_ekspresowy(self):
        account = CompanyAccount(self.company_name,self.nip)
        account.balance = 100
        account.zaksięguj_wychodzacy_przelew_ekspresowy(800)
        self.assertEqual(account.balance,100)



