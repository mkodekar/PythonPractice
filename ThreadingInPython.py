import threading
from queue import Queue as que
import time as t

print_lock = threading.Lock()

q = que()


def exampleJob(worker):
    t.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()


for x in range(10):
    th = threading.Thread(target=threader)
    th.daemon = True
    th.start()

start = t.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took', t.time() - start)
