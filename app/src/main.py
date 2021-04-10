import requests
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

from app.src.fizzbuzz import fb

def app(environ, start_response):
    """Application object"""
    if(environ.get("REQUEST_METHOD") == "GET"):
        if(environ.get("PATH_INFO") == "/"):
            status, data, headers = index()
        elif(environ.get("PATH_INFO") == "/joke"):
            status, data, headers = joke()
        elif(environ.get("PATH_INFO") == "/fizzbuzz"):
            number = parse_qs(environ.get("QUERY_STRING")).get("number")
            print(number)
            if(not number):
                status,data,headers = bad_request()
            else:
                status, data, headers = fizzbuzz(int(number[0]))
        else:
            status, data, headers = not_found()
        start_response(status, headers)
        return iter([data])
    else:
        status, data, headers = method_not_allowed()
        start_response(status, headers)
        return iter([data])


def make_basic_headers(data):
    return [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]

def joke():
    data = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt").text.encode('utf-8')
    return '200 OK', data, make_basic_headers(data)

def index():
    data = b"Hello World!"
    return '200 OK', data, make_basic_headers(data)

def fizzbuzz(number):
    data = fb(number).encode('utf-8')
    return '200 OK', data, make_basic_headers(data)

def not_found():
    data = b"404 Not Found"
    return '404 Not Found', data, make_basic_headers(data)

def bad_request():
    data = b"400 Bad Request"
    return '400 Bad Request', data, make_basic_headers(data)

def method_not_allowed():
    data = b'405 Method Not Allowed'
    return '405 Method Not Allowed', data, make_basic_headers(data)


# Make simple server if this is being run as main (gunicorn calls the application object directly).
if __name__ == "__main__":
    with make_server('', 8080, app) as srv:
        print("Serving app on port 8080...")
        srv.serve_forever()