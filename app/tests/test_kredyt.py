import unittest
# import parameterized


from ..Konto import Konto

class TestKredut(unittest.TestCase):
    imie = "Darek"
    nazwisko = "Kowalski"
    pesel = "1111111111"

    def setUp(self):
        self.konto = Konto(self.imie,self.nazwisko,self.pesel)

    
# @parameterized([
    #     ([-500,100,200,200],500,True,500),
    #     ([-500,100,200,200],500,True,500)

    # # ])
    # def test_testy(self,historia,kwota,oczekiwany_wynik,saldo):
    #     self.konto.historia = historia
    #     self.assertEqual(self.konto.zaciagnij_kredyt(kwota),True)
    #     self.assertEqual(self.konto.saldo,saldo,'Złe saldo konta')


    def test_zaciagnij_kredyt_udany_1(self):
        self.konto.historia = [1000,300,400]
        self.konto.saldo = sum(self.konto.historia)
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo + 500
        self.assertTrue(self.konto.zaciagnij_kredyt(500))
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_pusta_konto_1(self):
        self.konto.historia = []
        self.konto.saldo = sum(self.konto.historia)
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    
    def test_zaciagnij_kredyt_niudany_1_puste_konto(self):
        self.konto.historia = []
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo 
        self.assertFalse(self.konto.zaciagnij_kredyt(500))
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_zbyt_mało_trans_plus_1(self):
        self.konto.historia = [-500,100,200]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_zbyt_mało_trans_1(self):
        self.konto.historia = [200,300]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')


    def test_zaciagnij_kredyt_nieudany_1(self):
        self.konto.historia = [200,-500,100,500,200,-200]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_1_1(self):
        self.konto.historia = [100,-1]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo 
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_udany_2(self):
        self.konto.historia = [1000,-500,500,200,-200]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo + 500
        self.assertEqual(self.konto.zaciagnij_kredyt(500),True,'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')
    
    def test_zaciagnij_kredyt_udany_2_6_w_historii(self):
        self.konto.historia = [-1000,-500,500,200,-200,600]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo +500
        self.assertTrue(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_2(self):
        self.konto.historia = [-500,100,-500,300,200]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')

    def test_zaciagnij_kredyt_nieudany_2_rowno(self):
        self.konto.historia = [-100,100,-400,200,200]
        self.konto.saldo = sum(self.konto.historia)
        x = self.konto.saldo 
        self.assertFalse(self.konto.zaciagnij_kredyt(500),'Zła zwrócona wartość')
        self.assertEqual(self.konto.saldo,x,'Złe saldo konta')



   
    
        
        

