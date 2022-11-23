import re


class Konto:

    def __init__(self,imie,nazwisko,pesel,kod = None):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.saldo = 0
        self.pesel = pesel
        self.sprawdzenie_peselu(pesel)
        self.sprawdzenie_kodu_po_1960(kod)
        self.historia = []
        self.oplata = 1


    def sprawdzenie_peselu(self,pesel):
            if (len(pesel) != 11):
                self.pesel = "Niepoprawny pesel"
       

    def sprawdzenie_kodu_po_1960(self,kod_rabatowy):
         if (kod_rabatowy != None and re.fullmatch(r"PROM_.{3}",kod_rabatowy)):
            if(int(self.pesel[0:2]) > 60
               and  int(self.pesel[2:4]) < 81 ):
                self.saldo = self.saldo + 50
            elif(92 > int(self.pesel[2:4]) < 82 
                and int(self.pesel[2:3]) > 1
                and int(self.pesel[0:2]) < 60):
                self.saldo = self.saldo + 50

    def zaksięguj_przelew_wychodzący(self,kwota):
        if(self.saldo >= kwota and kwota > 0):
            self.saldo = self.saldo - kwota
            self.historia.append(-kwota)


    def zaksięguj_przelew_przychodzący(self,kwota):
        if(kwota >= 0):
            self.saldo = self.saldo + kwota
            self.historia.append(kwota)


    def zaksięguj_wychodzacy_przelew_ekspresowy(self,kwota):
        if(kwota <= self.saldo and kwota > 0 ):
            self.saldo = self.saldo - kwota - self.oplata 
            self.historia.append(-kwota)
            self.historia.append(-self.oplata)

    def zaciagnij_kredyt(self,kwota):
        last5 = self.historia[-5:]

        if(self.trzy_ostatnie(last5)):
            self.saldo += kwota 
            return True 
            
        elif(self.piec_ostatnich_i_wiecej(last5,kwota)):
            self.saldo += kwota
            return True
        else:
            return False
           

    def trzy_ostatnie(self,last5):
        if(len(last5) == 3):
            for i in last5:
                    if(i<0):         
                        return False
            return True

    def piec_ostatnich_i_wiecej(self,last5,kwota):
        if(len(last5) != 5): 
            return False
        suma = sum(last5)
        if(suma > kwota):
            return True
        else:
            return False 
       



   



               


        

        


   



