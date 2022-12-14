from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto
app = Flask(__name__)
@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201
@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return jsonify(len(RejestrKont.lista))
@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
     for i in RejestrKont.lista:
         if(i.pesel == pesel):
            return jsonify(imie = i.imie, nazwisko=i.nazwisko, pesel = i.pesel), 200
     return jsonify("To jest zły pesel")
    
