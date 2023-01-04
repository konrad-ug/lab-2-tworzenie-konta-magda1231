import unittest
from parameterized import parameterized

from ..Account import Account

class TestKredut(unittest.TestCase):
    name = "Darek"
    surname = "Kowalski"
    pesel = "1111111111"

    def setUp(self):
        self.account = Account(self.name,self.surname,self.pesel)

    
    @parameterized.expand([
        ([1000,300,400],500,True, 1700+500),
        ([],500,False,0),
        ([-500,100,200],500,False,-200),
        ([200,300],500,False,500),
        ([500,-500,100,500,200,-200],500,False,600),
        ([100,-1],500,False,99),
        ([1000,-500,500,200,-200],500,True,1500),
        ([-1000,-500,500,200,-200,600],500,True,100),
        ([-500,100,-500,300,200],500,False,-400),
        ([-100,100,-400,200,200],500,False,0)
        

    ])
    def test_testy(self,history,amount,oczekiwany_wynik,balance):
        self.account.history = history
        self.account.balance = sum(history)
        self.assertEqual(self.account.take_loan(amount),oczekiwany_wynik)
        self.assertEqual(self.account.balance,balance,'Złe balance accounts')



   
    
        
        

