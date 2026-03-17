import requests
import threading

target = "http://127.0.0.1:8080"

def send_request():
    while True:
        try:
            response = requests.get(target)
            print("Request sent", response.status_code)
        except:
            pass

for i in range(100):
    thread = threading.Thread(target=send_request)
    thread.start()
