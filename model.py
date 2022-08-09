# from msilib.schema import Class
from posixpath import split
import requests



# localhost:8000/ru/get_btc_price_by_currency/USD
# localhost:8000/ru/btc_cost/USD,124
class BtcPrice:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    btc_price = {}

    def __init__ (self):
        response = requests.get(self.url)
        api_response = response.json()
        self.btc_price = api_response
        # print(response)

    def get_price_by_currency(self, currency:str)->float:
        if self.btc_price["bpi"].get(currency):
            return self.btc_price["bpi"][currency]["rate_float"]
        else:
            return "Такой валюты не существует"

    def how_many_cost(self, btc_count:int, currency:str)->float:
        btc_rate = self.get_price_by_currency(currency)
        # print(type(btc_rate))
        return btc_rate * btc_count

# user.db
# login,password;login_2,password
class Auth:
    db_name:str = "user.db"

    def reg(self, login:str, password:str)->bool:
        with open( self.db_name, "r" ) as f:
            # print(f.read())
            users_data = f.read()
            user_list = users_data.split(";")
            # print(user_list)
            for i in user_list:
                user_login = i.split(",")[0]
                # print(user_login)
                if login == user_login:
                    print("Логин существует")
                    return 0

        with open( self.db_name, "a" ) as f:
            f.write(login + "," + password + ";")
        return 1 

    def auth(self, login:str, password:str)->bool:
        with open(self.db_name, "r") as f:
            user_data = f.read()
            user_list = user_data.split(";")
            for i in user_list:
                user_login = i.split(",")[0]
                print(user_login)
                if login == user_login:
                    user_pass = i.split(",")[1]
                    if password == user_pass:
                        return 1
            return 0


                    

if __name__ == "__main__":
    auth = Auth()
    # print(auth)
    auth.reg("vasya3", "45689")
    work_peremen = auth.auth("vasya3", "45789")
    
    print(work_peremen)
    



# class CharList:

# def __init__(self):

# def all_person():

# def 

# def func(some_data, some_data_2):
#     print("Asdasd")

# func("asdsad","sadsds")

