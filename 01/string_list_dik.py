numbers_str = "One Two Three Four Five Five"

numbers_list = numbers_str.split()

my_favorite_number = ("Five", "Two")
# Three = numbers_list[2]

count = 0
for i in numbers_list:
    if i in my_favorite_number:
        count = count + 1
         
# super_list = ((0,42), (18,00))
# print(super_list[0][1])

numers_dict = {
    "One"   : 1,
    "Two"   : 2,
    "Three" : 3,
    "Four"  : 4,
    "Five"  : 5,
    "Six"   : 6,  
}

# for k, i in numers_dict.items():
#     print(k, i)

sum = 0
print(numbers_list)
for i in numbers_list:
    # print(f"Слово из списка {i} равно {numers_dict[i]} в инт форме" )
    sum = sum + numers_dict[i]
    # print(numers_dict[i])

# print(sum)
# print(numers_dict["Three"])
# print(int("123"))

fucking_price = "9,999.99"
not_fucking_price = fucking_price.replace( ",", "")
items_count = 4
summ_data = 4 * float(not_fucking_price)
# print(summ_data)


float_string = "59,99"
float_string = float_string.replace(",",".")
print(float(float_string))


hard_dict = {
    "inner_dict" : {
        "inner_dict_key_1" : 1,
        "inner_dict_key_2" : 2,
    },
}

inner_dict = "inner_dict"
inner_dict_key_1 = "inner_dict_key_1"

print(hard_dict["inner_dict"]["inner_dict_key_2"])

# https://api.coindesk.com/v1/bpi/currentprice.json
    # Посчиать стоимость 10 битков в двух валютах
    # USD/EUR
    # carrents = ("USD", "EUR")
    # count    = 10    
    # Выводишь в косоль стоимость в каждой из валют
# Через библиотеку requests получаем ответ от API 
#     В ответе придет строка в формате json
# Этот отвает через библитеку json превращаем в структуру данных 

# https://api1.binance.com/api/v3/ticker/price
    # requests
    # json
    


