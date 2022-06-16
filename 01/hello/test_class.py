from curses import can_change_color
from http.client import MOVED_PERMANENTLY
from unicodedata import name


class Human:
    name = str()
    age = int()
    money = int()

    def __str__ (self):
        return f"Это {self.name}, ему {self.age} года"
    
    def __init__(self, name, age, money):
        self.age = age 
        self.name = name
        self.money = money
        
    def can_buy_beer(self):
        if self.age < 18:
            return False 
        else:
            return True

    def eat(self, food):
        print (f"{self.name} поел {food}")

    def go_to_the_cinema(self):
        cinema_price = 50
        if self.money < cinema_price:
            print (f"У {self.name} нет денег он слишком бедный")
        else:
            print (f"{self.name} сходил в кино")
            self.money = self.money - cinema_price

class Children(Human):
    
    def eat(self, food):
        if food != "konfeta":
            print("Не хочу нмчего кроме конфет")

        
human_dict = {
    1 : {
        "name" : "Александр",
        "age" : 33,
        "money" : 233
    },
    2 : { 
        "name" : "Fantomas",
        "age" : 144,
        "money" : 133
    },
    3 : {
        "name": "Матвей",
        "age" : 5,
        "money" : 33
    }
}

food = "apple"

for i in human_dict:
    if human_dict[i]["age"] < 12:
        human = Children(human_dict[i]["name"], human_dict[i]["age"], human_dict[i]["money"])
    else:
        human = Human(human_dict[i]["name"], human_dict[i]["age"], human_dict[i]["money"])
    
    human.eat(food)

    # for i in range(5):
    #     human.go_to_the_cinema()
    

    if human.can_buy_beer():
        print(f'{human.name} может купить пива' )
    else:
        print(f'{human.name} не может купить пива' )


# human = Human("Fantomas", 144)    
# human_2 = Human("Sasha", 33)

# # human.can_buy_beer()
# can_buy_beer = human.can_buy_beer()


# Проверяет, может ли человек купить пива.
# Если человеку меньше 18 лет, возвращается False, иначе True

# print(human_2)
# print(human)

# print(type(human))
# print(dir(human))



# [
#  '__init__',
#  '__str__',
#  'age',
#  'name'
#  ]