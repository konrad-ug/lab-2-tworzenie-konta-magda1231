import unittest

from ..Company_Account import CompanyAccount

class TestTworzenieaccountsFirmowego(unittest.TestCase):
    company_name = "Idk sp. zoo"
    nip = "1234567890"

    def test_tworzenie_accounts(self):
        account = CompanyAccount(self.company_name, self.nip )
        self.assertEqual(account.company_name,self.company_name, "Nazwa firmy nie została napisana")
        self.assertEqual(account.nip, self.nip, "Nip nie został zapisany")
        self.assertEqual(account.balance, 0, "Saldo nie jest 0")
        self.assertEqual(account.history, [] , "Zła początkowa history")

    def test_zbyt_długi_nip(self):
        account = CompanyAccount(self.company_name, self.nip + "123" )
        self.assertEqual(account.nip, "Niepoprawny NIP", "Niepoprawny nip zaaceptowany")

    def test_zbyt_krótki_nip(self):
        account = CompanyAccount(self.company_name, "123456" )
        self.assertEqual(account.nip, "Niepoprawny NIP", "Niepoprawny nip zaaceptowany")


