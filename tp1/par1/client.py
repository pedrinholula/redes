# coding: utf-8

import socket
import random
import string

HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
MESSAGES = 10  # Numero de mensagens a ser enviado
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

for x in range(MESSAGES):
    msg = random.choice(string.ascii_letters)*10
    print x, msg
    tcp.send(msg)
response = tcp.recv(8)
tcp.close()
print response
