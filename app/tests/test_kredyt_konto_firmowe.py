import unittest
from parameterized import parameterized

from ..Konto_firmowe import KontoFirmowe

class TestKredytKontoFirmowe(unittest.TestCase):
    nazwa = "al"
    nip = "111111111"

    def setUp(self):
        self.kontof = KontoFirmowe(self.nazwa,self.nip)

    
    @parameterized.expand([
        ([2000,-1775],225,100,True,325),
        ([2000],2000,500,False,2000),
        ([2000,-1775,2000,2000],4225,4000,False,4225),
        ([2000,1775],3775,1000,False,3775),
        ([],0,100,False,0)


     
        

    ])
    def test_testy(self,historia,saldoprzed,kwota,oczekiwany_wynik,saldo):
        self.kontof.historia = historia
        self.kontof.saldo = saldoprzed
        self.assertEqual(self.kontof.zaciagnij_kredyt(kwota),oczekiwany_wynik,"Zła wartość")
        self.assertEqual(self.kontof.saldo,saldo,'Złe saldo konta')