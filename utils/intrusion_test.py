from requests import request
import threading

def send_req(i):
    print('Request {} started'.format(i))
    request('POST', 'http://galiold.ir:8000')
    print('Request {} done'.format(i))

for i in range(11):
    t = threading.Thread(target=send_req, args=(i,))
    t.setDaemon(True)
    t.start()

while True:
    pass