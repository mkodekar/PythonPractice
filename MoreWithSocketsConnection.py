import socket
import sys as s
from _thread import *

host = ''
port = 5555

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((host, port))
except socket.error as e:
    print(str(e))

soc.listen(5)
print('Waiting for a connection')

def theader_client(conn):
    conn.send(str.encode('Welcome, type your info: '))
    while True:
        data = conn.recv(2048)
        reply = 'Server output is :' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn, add = soc.accept()
    print('connected to: ' + add[0] + str(add[1]))
    start_new_thread(theader_client, (conn,))
