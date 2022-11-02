import re
class Konto:
    def __init__(self,imie,nazwisko,pesel,kod = None):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.saldo = 0
        self.pesel = pesel
        self.sprawdzenie_peselu(pesel)
        self.sprawdzenie_kodu_po_1960(kod)
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
    def zaksięguj_przelew_przychodzący(self,kwota):
        if(kwota >= 0):
            self.saldo = self.saldo + kwota

    def zaksięguj_wychodzacy_przelew_ekspresowy(self,kwota):
        if(kwota <= self.saldo and kwota > 0 ):
            self.saldo = self.saldo - kwota - self.oplata 

    
        


   



               


        

        


   




