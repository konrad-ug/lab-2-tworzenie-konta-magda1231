import re


class Account:

    def __init__(self,name,surname,pesel,kod = None):
        self.name = name
        self.surname = surname 
        self.balance = 0
        self.pesel = pesel
        self.check_pesel(pesel)
        self.check_code_after_1960(kod)
        self.history = []
        self.charge = 1


    def check_pesel(self,pesel):
            if (len(pesel) != 11):
                self.pesel = "Niepoprawny pesel"
       

    def check_code_after_1960(self,promo_code):
         if (promo_code != None and re.fullmatch(r"PROM_.{3}",promo_code)):
            if(int(self.pesel[0:2]) > 60
               and  int(self.pesel[2:4]) < 81 ):
                self.balance = self.balance + 50
            elif(92 > int(self.pesel[2:4]) < 82 
                and int(self.pesel[2:3]) > 1
                and int(self.pesel[0:2]) < 60):
                self.balance = self.balance + 50

    def zaksięguj_przelew_wychodzący(self,amount):
        if(self.balance >= amount and amount > 0):
            self.balance = self.balance - amount
            self.history.append(-amount)


    def zaksięguj_przelew_przychodzący(self,amount):
        if(amount >= 0):
            self.balance = self.balance + amount
            self.history.append(amount)


    def zaksięguj_wychodzacy_przelew_ekspresowy(self,amount):
        if(amount <= self.balance and amount > 0 ):
            self.balance = self.balance - amount - self.charge 
            self.history.append(-amount)
            self.history.append(-self.charge)

    def take_loan(self,amount):
        last5 = self.history[-5:]

        if(self.last_3(last5)):
            self.balance += amount 
            return True 
            
        elif(self.last_5_and_more(last5,amount)):
            self.balance += amount
            return True
        else:
            return False
           

    def last_3(self,last5):
        if(len(last5) == 3):
            for i in last5:
                    if(i<0):         
                        return False
            return True

    def last_5_and_more(self,last5,amount):
        if(len(last5) != 5): 
            return False
        suma = sum(last5)
        if(suma > amount):
            return True
        else:
            return False 
       



   



               


        

        


   



