from app.Konto import Konto

class KontoFirmowe(Konto):

    def __init__(self,nazwa_firmy,nip):
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip if(self.sprawdzenie_nipu(nip)) else "Niepoprawny NIP"
        self.saldo = 0
        self.oplata = 5
        
    def sprawdzenie_nipu(self,NIP):
        if (len(NIP) != 10):
            return False
        else:
            return True

    def zaksięguj_przelew_wychodzący(self, kwota):
        return super().zaksięguj_przelew_wychodzący(kwota)

    def zaksięguj_przelew_przychodzący(self, kwota):
        return super().zaksięguj_przelew_przychodzący(kwota)
    
    
    def zaksięguj_wychodzacy_przelew_ekspresowy(self, kwota):
        return super().zaksięguj_wychodzacy_przelew_ekspresowy(kwota)
   

# konto = KontoFirmowe("aa","1111111111")
# print(konto.zaksięguj_wychodzacy_przelew_ekspresowy(5))