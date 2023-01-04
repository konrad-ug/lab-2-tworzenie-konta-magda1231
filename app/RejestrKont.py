from .Konto import Konto


class RejestrKont():
    lista=[]

    @classmethod
    def dodaj_konto(cls,konto):
        cls.lista.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)
        

    @classmethod
    def znajdz_konto(cls,pesel):
       for i in cls.lista:
         if(i.pesel == pesel):
            return i
       return "To jest zły pesel"
     

     #ok
    

