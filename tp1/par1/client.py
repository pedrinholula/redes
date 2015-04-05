# coding: utf-8

import socket
import random
import string
import sys

HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

if argc == 3:
    MESSAGES = argv[1]  # Numero de mensagens a ser enviado
    SIZE = argv[2]
else:
    print "Usage: client.py <# MESSAGES> <MESSAGES SIZE>"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

#Cria a lista de mensagens
msg_lst = []
for msg in range(MESSAGES):
    w = ''
    for size in range(SIZE):
        w += random.choice(string.ascii_letters)
    msg_lst.append(w)

#Envia uma a uma as mensagens criadas
for msg in msg_lst:
    print msg
    tcp.send(msg)
tcp.shutdown(socket.SHUT_WR)  # Fecha a conexão para envio
response = tcp.recv(8)  # Recebe a resposta do servidor
print response
tcp.close()
