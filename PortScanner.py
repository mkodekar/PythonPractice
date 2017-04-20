import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'


def scanPort(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False
for x in range(1, 30):
    if scanPort(x):
        print('Port', x, 'is open !!!!!!')
    else:
        print('Port', x, 'is closed')
