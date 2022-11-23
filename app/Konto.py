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

    # def zaciagnij_kredyt(self,kwota):
    #     last3 = self.historia[-3:] 
    #     if(len(last3) == 3):
    #         for i in last3:
    #                 if(i<0):
    #                     print(i)
    #                     return False
    #         self.saldo = self.saldo + kwota
    #         return True
    #     else:
    #         return False


    def zaciagnij_kredyt(self,kwota):
        last5 = self.historia[-5:]
        if(len(last5) == 3):
            for i in last5:
                    if(i<0):         
                        return False
            self.saldo=self.saldo+ kwota
            return True
        if(len(last5) == 5): 
            suma = 0
            for i in last5:
                suma = suma + i 
            if(suma > kwota):
                self.saldo = self.saldo + kwota
                return True
            else:
                return False 
        else:
            return False 

# konto = Konto("Ala","Kowalska","1111111111")
# konto.zaciagnij_kredyt(500)
# historia = [1000,-500,500,200,-200]
# historia = [1000,-500,500,200,-200]
# def zaciagnij_kredyt(kwota):
#         saldo = 1000
#         last3 = historia[-3:]
#         last5 = historia[-5:] 
#         if(len(last3) == 3 and len(last5) != 5):
#             for i in last3:
#                     if(i<0):
#                         print(i)
#                         return False
#             saldo = saldo + kwota
#             return True
#         elif(len(last5)== 5):
#             suma = 0
#             for i in last5:
#                 suma += i
#             if(suma>0):
#                 return True
#             else:
#                 return False 
#         else:
#             return False 
            
# print(zaciagnij_kredyt(500))

# last5 = historia[-5:]
# suma = 0
# for i in last5:
#     suma += i
# print(suma)
# historia = [1000,300,400]
# saldo = 1700
# def zaciagnij_kredyt(kwota):
        

#         last5 = historia[-5:]
#         if(len(last5) == 3):
#             for i in last5:
#                     if(i<0):         
#                         return False
#             saldo = saldo+kwota
#             print(saldo)
#             return True
#         if(len(last5) == 5): 
#             suma = 0
#             for i in last5:
#                 suma = suma + i 
#             if(suma > kwota):
#                 saldo = saldo + kwota
#                 return True
#             else:
#                 return False 
#         else:
#             return False 

# zaciagnij_kredyt(500)
        



   



               


        

        


   




historia = [1000,-500,500,200,-200]
print(sum(historia))