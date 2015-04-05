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
    #Envia uma a uma as mensagens criadas
    for msg in create_messages(MESSAGES, SIZE):
        print msg


if len(sys.argv) == 3:
    MESSAGES = int(sys.argv[1])  # Numero de mensagens a ser enviado
    SIZE = int(sys.argv[2])
    t = timeit.Timer(client)
    print t.repeat(4, 100)
else:
    print "Usage: client.py <#MESSAGES> <MESSAGES SIZE>"
    sys.exit()
