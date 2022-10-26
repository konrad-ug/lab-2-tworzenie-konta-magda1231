import re
class Konto:
    def __init__(self,imie,nazwisko,pesel,kod = None):
        self.imie = imie
        self.nazwisko = nazwisko 
        self.saldo = 0
        self.pesel =  pesel if (len(pesel) == 11) else  "Niepoprawny pesel"
        if (kod != None and re.fullmatch(r"PROM_.{3}",kod)):
            self.saldo = self.saldo + 50


   




