import unittest
import requests

class TestObsługaKont(unittest.TestCase):
    body = {
        "name":"ala",
        "surname":"makota",
        "pesel":"12345678901"
    }
    new_body = {
        "name":"Ala",
        "surname":"niemakota",
        'balance':11
    }
    url="http://localhost:5000"
    

    def test_1_create_account_right(self):
        resp = requests.post(self.url + "/accounts/create_account", json = self.body)
        self.assertEqual(resp.status_code,201)

    def test_2_get_with_pesel(self):
        resp = requests.get(self.url + f"/accounts/account/{self.body['pesel']}")
        self.assertEqual(resp.status_code,200)
        resp_body = resp.json()
        self.assertEqual(resp_body["name"], self.body["name"])
        self.assertEqual(resp_body["surname"], self.body["surname"])
        self.assertEqual(resp_body["balance"], 0)

    def test_3_put(self):
        resp = requests.put(self.url + f"/accounts/update_account/{self.body['pesel']}",json = self.new_body) 
        self.assertEqual(resp.status_code,200)
        resp_body = resp.json()
        self.assertEqual(resp_body["name"], self.new_body["name"])
        self.assertEqual(resp_body["surname"], self.new_body["surname"])
        self.assertEqual(resp_body["balance"], self.new_body["balance"])

    def test_4_delete(self):
        resp = requests.delete(self.url + f"/accounts/delete_account/{self.body['pesel']}")
        self.assertEqual(resp.status_code,200)
        resp_body = resp.json()
        self.assertEqual(resp_body, "Usunięto konto")

    def test_5_accounts_ammount(self):
        resp = requests.get(self.url + "/accounts/amount_of_accounts")
        self.assertEqual(resp.status_code,200)
        resp_body = resp.json()
        self.assertEqual(resp_body, 0)

    def test_5_create_account_existing_pesel(self):
        resp = requests.post(self.url + "/accounts/create_account", json = self.body)
        resp = requests.post(self.url + "/accounts/create_account", json = self.body)
        self.assertEqual(resp.status_code,404)
        resp_body = resp.json()
        self.assertEqual(resp_body, "To konto już istnieje")


        ####


        




        
    







  
