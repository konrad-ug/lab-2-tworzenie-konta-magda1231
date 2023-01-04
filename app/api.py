from flask import Flask, request, jsonify
from app.AccountRegister import AccountRegister
from app.Account import Account
app = Flask(__name__)

def create_account():
    data = request.get_json()
    print(f"Request o stworzenie accounts z danymi: {data}")
    account = Account(data["name"], data["surname"], data["pesel"])
    if AccountRegister.add_account(account) != "To konto już istnieje":
        return jsonify("Account stworzone"), 201
    return jsonify("To konto już istnieje"), 400


@app.route("/accounts/amount_of_accounts", methods=['GET'])
def amount_of_accounts():
    return jsonify(len(AccountRegister.list))

@app.route("/accounts/account/<pesel>", methods=['GET'])
def find_account(pesel):
     for i in AccountRegister.list:
         if(i.pesel == pesel):
            print("Wyszukaj")
            return jsonify(name = i.name, surname=i.surname, pesel = i.pesel, balance=i.balance ), 200
     return jsonify("To jest zły pesel"), 404
    
@app.route("/accounts/update_account/<pesel>", methods=['PUT'])
def change_account_data(pesel):
    account = AccountRegister.find_account(pesel)
    data = request.get_json()
    if(account != "To jest zły pesel"):
        print("Aaa")
        updated_account = AccountRegister.update_account(pesel,data)
        return jsonify(name = updated_account.name,surname=updated_account.surname,balance=updated_account.balance), 200
    return jsonify("Zły"),404

@app.route("/accounts/delete_account/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    account = AccountRegister.find_account(pesel)
    if(account != "To jest zły pesel"):
        AccountRegister.delete_account(pesel)
        return jsonify("Usunięto konto"), 200
    return jsonify("Zły"),404





























    
        









    
    
