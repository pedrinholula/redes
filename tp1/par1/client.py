import socket
import random
import string

HOST = '10.0.0.1' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
response = True
ba = []
for x in range(1000):
    ba.append (random.choice(string.ascii_letters))
ss=StreamSocket(tcp,Raw)
while response <> '0':
    for msg in ba:
        print msg
        ss.send (Raw(msg))
        response = tcp.recv(1024)
        print response
tcp.close()
