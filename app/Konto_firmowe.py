from app.Konto import Konto


class KontoFirmowe(Konto):

    def __init__(self,nazwa_firmy,nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if(self.sprawdzenie_nipu(nip)) else "Niepoprawny NIP"
        self.saldo = 0
        self.historia = []
        self.oplata = 5
        

    def sprawdzenie_nipu(self,NIP):
        if (len(NIP) != 10):
            return False
        else:
            return True

    def zaciagnij_kredyt(self, kwota):
       if (self.saldo >= kwota*2 and (-1775 in self.historia)):
            self.saldo += kwota
            return True
       else:
            return False 
