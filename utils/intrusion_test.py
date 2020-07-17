from requests import request
import threading

def send_req():
    request('POST', 'http://galiold.ir:8000')

for i in range(11):
    t = threading.Thread(target=send_req)
    t.setDaemon(True)
    t.start()
    if i == 10:
        t.join()