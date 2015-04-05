# coding: utf-8

import socket
import random
import string
import sys


def create_messages(numM, sizeM):
    #Cria a lista de mensagens
    msg_lst = []
    for msg in range(numM):
        w = ''
        for size in range(sizeM):
            w += random.choice(string.ascii_letters)
        msg_lst.append(w)
    return msg_lst


def client():
    #Faz a conexão cliente servidor
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    #Envia uma a uma as mensagens criadas
    for msg in create_messages(MESSAGES, SIZE):
        print msg
        tcp.send(msg)
    tcp.shutdown(socket.SHUT_WR)  # Fecha a conexão para envio
    response = tcp.recv(8)  # Recebe a resposta do servidor
    print response
    tcp.close()


HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
#Numero de mensagens e tamanho de cada uma
if len(sys.argv) == 3:
    MESSAGES = int(sys.argv[1])  # Numero de mensagens a ser enviado
    SIZE = int(sys.argv[2])
else:
    print "Usage: client.py <# MESSAGES> <MESSAGES SIZE>"
    sys.exit()
client()
