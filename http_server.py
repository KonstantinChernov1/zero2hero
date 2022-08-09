from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
# from posixpath import split
import view 
import json

def render(data, error = ""):
    result_data = {
        "result" : data,
        "error" : error,
    }
    return json.dumps(result_data, ensure_ascii=False)

# numbers_text = "one,two,three,four"

# /ru/reg/login,password
# /ru/get_posts/34234,12312312
def dispath(path:str)->list:
    path_list = path.split("/")
    # ['', 'ru', 'get_post', '34234']
    if len(path_list) < 3:
        return ("favicon", "")
    print(path_list)

    action = path_list[2]
    param = path_list[3].split(",")

    return [action, param]

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        result = ""
        action, param = dispath(self.path)
        # print(view.rout_dict)
        
        # Если ключа не будет вернёт Nonefffff
        # view.rout_dict.get(action)

        # Если ключа не будет, выпадет с ошибкой ( исколючение )
        # view.rout_dict[action]

        if view.rout_dict.get(action):
            result = view.rout_dict[action](*param)
        else:
            result = view.rout_dict["404"]()

        result_str = render(result)
        self.wfile.write(result_str.encode())

# localhost:8000/ru/say_name/Ivan
# localhost:8000/ru/get_post/34234
# https:// - Зашифрованный http 
# habr.com - Домен ( который на самом деле языковая конструкция ссылающаяся на ip адрес)
# /ru - языковой параметр
# /get_post - action - действие которое необходимо удаленно вызвать
# /672646  - Параметр, который мы должны передать в наш action

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('localhost', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run()