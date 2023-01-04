import unittest
from parameterized import parameterized

from ..Konto import Konto

class TestKredut(unittest.TestCase):
    imie = "Darek"
    nazwisko = "Kowalski"
    pesel = "1111111111"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    
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
    def test_testy(self,historia,kwota,oczekiwany_wynik,saldo):
        self.konto.historia = historia
        self.konto.saldo = sum(historia)
        self.assertEqual(self.konto.zaciagnij_kredyt(kwota),oczekiwany_wynik)
        self.assertEqual(self.konto.saldo,saldo,'Złe saldo konta')



   
    
        
        

