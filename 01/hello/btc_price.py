import json
from unicodedata import name
# import requests


class Human:
    human_name = "Иван"
    fraza = "Некая фраза"

    def __init__(self, name, fraze):
        self.human_name = name
        self.fraza = fraze
        

    def get_human_name(self):
        return self.human_name    

    def upper_human_name(self):
        return self.human_name.upper()

    # Возвращается такая строка
    # ИВАН говорит фроазу Некая фараза 
    def human_say(self):
        print( self.upper_human_name() + " говорит фроазу "  + self.fraza )

    def human_say_another_fraze(self, outer_fraze):
        print(outer_fraze)


name = "Всеволод"
fraze = "Это другая некая фраза"
human = Human(name, fraze)

outer_fraze  = "Я есть человек"
human.human_say()
human.human_say_another_fraze(outer_fraze)


name_2 = "Василий"
fraze_2 = "Фраза Василия"
human2 = Human(name_2, fraze_2)
human2.human_say()
human2.human_say_another_fraze(outer_fraze)

# print(human.fraza)

# Класс на вход принимает список цен 
# У класса есть метод, по которому мы можем получить стоимость btc  по курсу валюты 
# У класса есть метод, который принимает Имя валюты и кол-во btc, выдает сколько стоит кол-во btc В этой валюте

class BtcPrice:
    btc_price = {}

    def __init__(self, api_data) -> None:
        if not isinstance(api_data, dict):
            raise ValueError("Api data не является словарем")

        self.btc_price = api_data



def get_data_by_api(url:str)->dict:
    response = requests.get(url)
    api_response = response.json()
    return api_response

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
my_fav_bpi = ["USD", "EUR"]
btc_cnt = 10
total_money = 10000

api_data = get_data_by_api(url)

# btc_price_obj = BtcPrice(api_data)
# result  = BtcPrice.btc_calculate("USD", btc_cnt)
# print(btc_price_obj.btc_price)

# class BeerMag:
#     mag_name = "Самый лучший магазин пива"
#     price_list = {}

#     def __init__(self, price_list):
#         self.price_list = price_list

#     def __str__(self):
#         return self.mag_name

#     def get_low_price_beer(self):
#         tmp_dict = {
#             "beer_name" : "",
#             "beer_price": 0
#         }

#         count = 0 
#         for i in self.price_list:
#             if not count:
#                 tmp_dict["beer_name"] = i
#                 tmp_dict["beer_price"] = self.price_list[i]
#                 count += 1
            
#             if self.price_list[i] < tmp_dict["beer_price"]:
#                 tmp_dict["beer_name"] = i
#                 tmp_dict["beer_price"] = self.price_list[i]

                 
#         return tmp_dict
#     def print_low_pirce_beer(self):
#         print(self.get_low_price_beer())

# price_list = {
#     "Жигули": 114,
#     "Бад": 144,
#     "Козел": 104,
#     "Бойлероное": 90,
# }
# price_list_2 = {
#     "Жигули": 114,
#     "Козел": 1005055,
#     "Бойлероное": 90,
# }

# # BeerMag.object_construct.__init__(price_list)
# beer_mag_obj =  BeerMag(price_list)
# # beer_mag_2 = BeerMag(price_list_2)
# # print(beer_mag_obj.get_low_price_beer())
# beer_mag_obj.print_low_pirce_beer()
# # print(dir(beer_mag_obj))
# # self.get_low_price_beer()
# # print(type(beer_mag_obj))
# # print(dir(beer_mag_obj))
# # <__main__.BeerMag object at 0x7f8adb84b370>
# # print()
# # value = 10000
# # print( type( value.__str__() ) )

# def main():
#     if func_dict.get("func"):
#         func_dict.get("func")()
#     else:
#         one()

# def one():
#     pass

# def two():
#     print("Func Two")

# func_dict = {
#     # "func" : two,
# }

# # main()

# # print(dir(18))
# # print(dir("asdasdsa"))
# # print(dir(False))
# # print(dir({}))
# # print(dir([]))
# # print(dir(None))