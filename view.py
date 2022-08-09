from distutils.log import error
from fileinput import close
from unittest import result
import model


rout_dict = {}

def router(path:str):
    def actual_decorator(func):
        # print(func.__name__)
        # print(func)
        rout_dict[path]  = func

        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            return func
        
        return wrapper
    return actual_decorator

@router("auth")
def auth(login:str, password:str)->str:
    if auth.auth == 0:
        return "Логин или пароль не совпадает"
    else:
        return "Вы залогинились!!!" 



@router("get_post")
def get_post(post_id):
    return f"Это пост с номером {post_id}"

# /ru/reg/login,passworddd
@router("reg")
def reg(login:str, password:str)->str:
    if len(password) < 4:
        return "Пароль слишком короткий"
    auth_object = model.Auth()
    result = auth_object.reg(login, password)
    if result:
        return "Поздравляем вы успешно зарегестрировались"
    else:
        return "Такой пользователь существует!!!!"

# /ru/get_btc_price_by_currency/USD
@router('get_btc_price_by_currency')
def get_btc_price_by_currency(currency:str):
    btc_price = model.BtcPrice()
    result = btc_price.get_price_by_currency(currency)
    if result:
        return f"Стоимость BTC в валюте {currency} = {result}"
    else:
        return f"Валюты {currency} нет в нашей БД"


@router("say_name")
def say_my_name(name:str)->str:
    return {
        "Имя" : name,
        "Фамилия" : "Неизвестно"
    }

@router("404")
def page_not_found():
    return "404 Страница не найдена"

# localhost:8000/ru/some_method/param
@router("some_method")
def some_method(paran):
    return "asdasds"



@router('btc_cost')
def btc_cost(currency:str, btc_count:str):
    btc_obj = model.BtcPrice()
    return btc_obj.how_many_cost(int(btc_count), currency)

def test_def():
    return "Текс функции test_def"

if __name__ == "__main__":
    print("Мы ничего не запускаем из функций")
    # print(rout_dict)
    # print(rout_dict["404"])
    rout_dict["Test_DEF"] = test_def

    # print( test_def() )
    # print( rout_dict["Test_DEF"]() )


    # print( test_def() )
    # print( rout_dict["Test_DEF"]() )
    # print(page_not_found)
    # some_data = {
    #     "func" : say_my_name
    # }
    
    # print(some_data["func"]("Ivan"))