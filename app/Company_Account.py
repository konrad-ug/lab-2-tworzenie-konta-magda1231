from app.Account import Account


class CompanyAccount(Account):

    def __init__(self,company_name,nip):
        self.company_name = company_name
        self.nip = nip if(self.check_nip(nip)) else "Niepoprawny NIP"
        self.balance = 0
        self.history = []
        self.charge = 5
        

    def check_nip(self,NIP):
        if (len(NIP) != 10):
            return False
        else:
            return True

    def take_loan(self, amount):
       if (self.balance >= amount*2 and (-1775 in self.history)):
            self.balance += amount
            return True
       else:
            return False 
