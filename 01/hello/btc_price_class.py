import requests

class BtcPrice:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    btc_price = {}

    def __init__ (self):
        response = requests.get(self.url)
        api_response = response.json()
        self.btc_price = api_response
        # print(response)

    def get_price_by_currency(self, currency):
        if self.btc_price["bpi"].get(currency):
            return self.btc_price["bpi"][currency]["rate_float"]
        else:
            return "Такой валюты не существует"

    def how_many_cost(self, btc_count, currency):
        btc_rate = self.get_price_by_currency(currency)
        print(type(btc_rate))
        return btc_rate * btc_count

btc_count = 10

btc_price = BtcPrice()

print(btc_price.get_price_by_currency("USD"))

print(btc_price.how_many_cost(btc_count, "EUR"))

