import unittest

from ..AccountRegister import AccountRegister
from .. Account import Account

class TestAccountRegister(unittest.TestCase):
    name = "Darek"
    name2 = "Darek"
    surname = "Kowalski"
    surname2 = "Kowalski"
    pesel = "11111111111"
    pesel2 = "12111111111"
    pesel3 = "01111111111"
    pesel4 = "02111111111"
    pesel5 = "02311111111"
    pesel6 = "02311111111"

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

   
    def test_1_add_account(self):
        account = Account(self.name,self.surname,self.pesel)
        AccountRegister.add_account(account)
        self.assertEqual(AccountRegister.amount_of_accounts(),1)


    def test_2_dodaj_2_accounts(self):
        account2 = Account(self.name,self.surname,self.pesel2)
        account3 = Account(self.name2,self.surname2,self.pesel3)
        AccountRegister.add_account(account2)
        AccountRegister.add_account(account3)
        self.assertEqual(AccountRegister.amount_of_accounts(),3)

    def test_3_amount_of_accounts(self):
        AccountRegister.amount_of_accounts()
        self.assertEqual(AccountRegister.amount_of_accounts(),3)

    def test_4_find_po_peselu(self):
        account4 = Account(self.name,self.surname,"21111111111")
        AccountRegister.add_account(account4)
        self.assertEqual(AccountRegister.find_account("21111111111"),account4)

    def test_5_find_po_peselu_zły_pesel(self):
        self.assertEqual(AccountRegister.find_account("111111111"),"To jest zły pesel")

    def test_6_zmiana_danych(self):
        account5 = Account(self.name,self.surname,self.pesel4)
        AccountRegister.add_account(account5)
        account_aktualizacja = AccountRegister.update_account(self.pesel4,self.data)
        self.assertEqual(account_aktualizacja.name, self.data['name'])
        self.assertEqual(account_aktualizacja.surname, self.data['surname'])
        self.assertEqual(account_aktualizacja.balance, self.data['balance'])

    def test_7_delete_account(self):
        account6 = Account(self.name,self.surname,self.pesel5)
        AccountRegister.add_account(account6)
        AccountRegister.delete_account(self.pesel5)
        self.assertEqual(AccountRegister.amount_of_accounts(),5)

    def test_8_delete_account_zły_pesel(self):
        AccountRegister.delete_account("111111111")
        self.assertEqual(AccountRegister.amount_of_accounts(),5)

    def test_9_create_account_existing_pesel(self):
        account7 = Account(self.name,self.surname,self.pesel)
        AccountRegister.add_account(account7)
        self.assertEqual(AccountRegister.amount_of_accounts(),5)






