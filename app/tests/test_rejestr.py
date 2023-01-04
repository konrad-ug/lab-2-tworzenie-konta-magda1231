import unittest

from ..AccountRegister import AccountRegister
from .. Account import Account

class TestAccountRegister(unittest.TestCase):
    name = "Darek"
    name2 = "Darek"
    surname = "Kowalski"
    surname2 = "Kowalski"
    pesel = "11111111111"
    pesel1 = "11111111112"
    pesel2 = "11111111110"
    pesel3 = "01111111111"
    pesel4 = "01111111113"
    pesel5 = "01111111113"
    pesel6 = "01111111114"

    data = {
        "name": "Ala",
        "surname":"Makota",
        "balance":200
    }

    @classmethod
    def setUpClass(cls):
        account = Account(cls.name,cls.surname,cls.pesel)
        AccountRegister.add_account(account)

    @classmethod
    def tearDownClass(cls):
        AccountRegister.list = []

    def test_01_amount_of_accounts(self):
        self.assertEqual(AccountRegister.amount_of_accounts(),1)

    def test_02_add_account(self):
        account2 = Account(self.name,self.surname,self.pesel2)
        AccountRegister.add_account(account2)
        self.assertEqual(AccountRegister.amount_of_accounts(),2)

    def test_04_find(self):
        account4 = Account(self.name,self.surname,"21111111111")
        AccountRegister.add_account(account4)
        self.assertEqual(AccountRegister.find_account("21111111111"),account4)

    def test_05_find_bad_pesel(self):
        self.assertEqual(AccountRegister.find_account("111111111"),"To jest zły pesel")

    def test_06_update_data(self):
        account5 = Account(self.name,self.surname,self.pesel5)
        AccountRegister.add_account(account5)
        account_aktualizacja = AccountRegister.update_account(self.pesel5,self.data)
        self.assertEqual(account_aktualizacja.name, self.data['name'])
        self.assertEqual(account_aktualizacja.surname, self.data['surname'])
        self.assertEqual(account_aktualizacja.balance, self.data['balance'])

    def test_07_update_data_bad_pesel(self):
        self.assertEqual(AccountRegister.update_account("111111111",self.data),"To jest zły pesel")

    def test_08_delete_account(self):
        account6 = Account(self.name,self.surname,self.pesel6)
        AccountRegister.add_account(account6)
        AccountRegister.delete_account(self.pesel)
        self.assertEqual(AccountRegister.amount_of_accounts(),4)

    def test_09_delete_account_bad_pesel(self):
        AccountRegister.delete_account("111111111")
        self.assertEqual(AccountRegister.amount_of_accounts(),4)

    def test_10_create_account_existing_pesel(self):
        account7 = Account(self.name,self.surname,self.pesel)
        self.assertEqual(AccountRegister.amount_of_accounts(),4)



 


