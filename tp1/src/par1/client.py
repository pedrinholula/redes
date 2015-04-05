# coding: utf-8

import socket
import random
import string
import sys
import timeit


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
        #print msg
        tcp.send(msg)
    tcp.shutdown(socket.SHUT_WR)  # Fecha a conexão para envio
    response = tcp.recv(8)  # Recebe a resposta do servidor
    #print response
    tcp.close()


HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
if len(sys.argv) == 3:
    MESSAGES = int(sys.argv[1])  # Numero de mensagens a ser enviado
    SIZE = int(sys.argv[2])  # Tamanho de cada mensagem
    f = open('./resultp1-'+sys.argv[1]+'-'+sys.argv[2]+'.txt', 'w')
    t = timeit.Timer(client)

    exectime = t.repeat(4, 100)
    for item in exectime:
        print>>f, item

    f.close()
else:
    print "Usage: client.py <# MESSAGES> <MESSAGES SIZE>"
    sys.exit()
