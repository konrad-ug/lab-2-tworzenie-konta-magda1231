import unittest

from ..AccountRegister import AccountRegister
from .. Account import Account

class TestAccountRegister(unittest.TestCase):
    name = "Darek"
    name2 = "Darek"
    surname = "Kowalski"
    surname2 = "Kowalski"
    pesel = "11111111111"
    pesel2 = "11111111111"
    pesel3 = "01111111111"

    data = {
        "name": "Ala",
        "surname":"Makota",
        "balance":200
    }

    @classmethod
    def SetUpClass(cls):
        cls.account = Account(cls.name,cls.surname,cls.pesel)
        AccountRegister.add_account(cls.account)
        
    @classmethod
    def tearDownClass(cls):
        AccountRegister.list = []

    def test_0_no_accounts(self):
        self.assertEqual(AccountRegister.amount_of_accounts(),0)


    def test_1_add_account(self):
        account = Account(self.name,self.surname,self.pesel)
        AccountRegister.add_account(account)
        self.assertEqual(AccountRegister.amount_of_accounts(),1)

    def test_2_dodaj_2_account(self):
        account2 = Account(self.name,self.surname,self.pesel)
        AccountRegister.add_account(account2)
        self.assertEqual(AccountRegister.amount_of_accounts(),2)

    def test_3_amount_of_accounts(self):
        AccountRegister.amount_of_accounts()
        self.assertEqual(AccountRegister.amount_of_accounts(),2)

    def test_4_find_po_peselu(self):
        account4 = Account(self.name,self.surname,"21111111111")
        AccountRegister.add_account(account4)
        self.assertEqual(AccountRegister.find_account("21111111111"),account4)

    def test_5_find_po_peselu_zły_pesel(self):
        self.assertEqual(AccountRegister.find_account("111111111"),"To jest zły pesel")

    def test_6_zmiana_danych(self):
        account5 = Account(self.name,self.surname,self.pesel3)
        AccountRegister.add_account(account5)
        account_aktualizacja = AccountRegister.update_account(self.pesel3,self.data)
        self.assertEqual(account_aktualizacja.name, self.data['name'])
        self.assertEqual(account_aktualizacja.surname, self.data['surname'])
        self.assertEqual(account_aktualizacja.balance, self.data['balance'])

    def test_7_zmiana_danych_zły_pesel(self):
        self.assertEqual(AccountRegister.update_account("111111111",self.data),"To jest zły pesel")

    def test_7_delete_account(self):
        account6 = Account(self.name,self.surname,self.pesel)
        AccountRegister.add_account(account6)
        AccountRegister.delete_account(self.pesel)
        self.assertEqual(AccountRegister.amount_of_accounts(),4)

    def test_8_delete_account_zły_pesel(self):
        AccountRegister.delete_account("111111111")
        self.assertEqual(AccountRegister.amount_of_accounts(),4)



 


