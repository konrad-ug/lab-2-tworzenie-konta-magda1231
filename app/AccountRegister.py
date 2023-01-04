from .Account import Account


class AccountRegister():
    list=[]

    @classmethod
    def add_account(cls,account):
         if cls.find_account(account.pesel) == "To jest zły pesel":
           cls.list.append(account)
           return
         else :
             return "Ten pesel już istnieje"

    @classmethod
    def amount_of_accounts(cls):
        return len(cls.list)
        

    @classmethod
    def find_account(cls,pesel):
       for i in cls.list:
         if(i.pesel == pesel):
            return i
       return "To jest zły pesel"

    @classmethod
    def update_account(cls,pesel,new_data):
        account = cls.find_account(pesel)
        if account != "To jest zły pesel":
            if 'name' in new_data:
                account.name = new_data['name']
            if 'surname' in new_data:
                account.surname = new_data['surname']
            if 'balance' in new_data:
                account.balance = new_data['balance']
        return account
    
    @classmethod
    def delete_account(cls,pesel):
        account = cls.find_account(pesel)
        if account != "To jest zły pesel":
            cls.list.remove(account)
        return account
    



    
     
    

