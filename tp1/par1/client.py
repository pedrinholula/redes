# coding: utf-8

import socket
import random
import string

HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
MESSAGES = 10  # Numero de mensagens a ser enviado
SIZE = 10

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

msg_lst = []
for msg in range(MESSAGES):
    w = ''
    for size in range(SIZE):
        w += random.choice(string.ascii_letters)
    msg_lst.append(w)


for msg in msg_lst:
    print x, msg
    tcp.send(msg)
tcp.shutdown(socket.SHUT_WR)
response = tcp.recv(8)
print response
tcp.close()
