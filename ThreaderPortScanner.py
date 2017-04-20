import socket
import threading
from queue import Queue

print_lock = threading.Lock()
q = Queue()

target = 'pythonprogramming.net'


def portScanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open !!')
        con.close()
    except:
        pass


def theader():
    while True:
        worker = q.get()
        portScanner(worker)
        q.task_done()


for x in range(100):
    t = threading.Thread(target=theader)
    t.daemon = True
    t.start()

for worker in range(1, 1001):
    q.put(worker)


q.join()
