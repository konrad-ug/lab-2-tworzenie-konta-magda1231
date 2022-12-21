import unittest
from parameterized import parameterized

from ..Company_Account import CompanyAccount

class TestLoanCompanyAccount(unittest.TestCase):
    nazwa = "al"
    nip = "111111111"

    def setUp(self):
        self.accountf = CompanyAccount(self.nazwa,self.nip)

    
    @parameterized.expand([
        ([2000,-1775],225,100,True,325),
        ([2000],2000,500,False,2000),
        ([2000,-1775,2000,2000],4225,4000,False,4225),
        ([2000,1775],3775,1000,False,3775),
        ([],0,100,False,0)
     

    ])
    def test_testy(self,history,balanceprzed,amount,oczekiwany_wynik,balance):
        self.accountf.history = history
        self.accountf.balance = balanceprzed
        self.assertEqual(self.accountf.take_loan(amount),oczekiwany_wynik,"Zła wartość")
        self.assertEqual(self.accountf.balance,balance,'Złe balance accounts')