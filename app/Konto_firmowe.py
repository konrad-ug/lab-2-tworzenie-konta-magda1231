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
