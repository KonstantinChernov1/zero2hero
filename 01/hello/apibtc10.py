import json
import requests
#import test_modele

# Получаем днные из внешнего API в формате JSON
# Возвращаем их в python структуре данных
def get_data_by_api(url:str)->dict:
    response = requests.get(url)
    api_response = response.json()
    return api_response

# Функция принимает два значения 
# Одно значение типа float, второе типа int
# Должна вернуть произвеление одного числа на другое
def btc_calculate(rate:float, btc_cnt:int)->float :
    result = rate * btc_cnt
    return result

# Функция, принимае значнеие валюты 
# Возвращает стоимость биткойна в этой валюте
def get_btc_rate(api_response:dict, carrency:str)->float:
    btc_rate_str = api_resonse["bpi"][carrency]["rate"]
    btc_rate_float = float(btc_rate_str.replace( ",", ""))
    return btc_rate_float

def get_btc_count(total_money:int, btc_price:float)->float:
    return total_money/btc_price


if __name__ == "__main__":
    # Данные для запуска программы 
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    my_fav_bpi = ["USD", "EUR"]
    btc_cnt = 10
    total_money = 10000
    # Получение внешних данных
    # Из БД, Файла, API
    
    api_resonse = get_data_by_api(url)

    for i in my_fav_bpi:
        
        btc_rate = get_btc_rate(api_resonse, i)
        result = btc_calculate(btc_rate, btc_cnt)
        print(f"{btc_cnt} биткоинтов в валюте {i} стоит {result} {i}")


# Давай выделим функции get_btc_count и btc_calculate в отдельный модуль
# Подключим сюда модуль 
# Устанавливаем pytest/UnitTests
# Пишем простые тесты. Один тест на истину, второй тест ломающий (UnitTests)




















    # Общая бизнес логика
    # bpi_dict = api_resonse["bpi"]
    # for i in bpi_dict:
    #     if i in my_fav_bpi:
    #         fav_bpi_rate = bpi_dict[i]["rate"]
    #         fav_bpi_rate_float = float(fav_bpi_rate.replace( ",", ""))

    #         # Core логика
    #         
    #         print(result)


    # return api_resonse
    # def in_list(value):
    #     for i in my_fav_bpi:
    #         if i == value:
    #             return True
        
    #     return False
 