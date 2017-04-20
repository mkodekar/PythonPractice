import socket

host = ''
port = 5555

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    soc.bind((host, port))
except socket.error as e:
    print(str(e))

soc.listen(5)

conn, add = soc.accept()

print('connected to: ' + add[0] + str(add[1]))
