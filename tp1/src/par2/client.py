# coding: utf-8
import sys
import timeit
import numpy


def create_messages(num, size):
    #Cria a lista de mensagens
    import random
    import string
    msg_lst = []
    for msg in range(num):
        w = ''
        for size in range(size):
            w += random.choice(string.ascii_letters)
        msg_lst.append(w)
    return msg_lst


def client():
    #Client socket
    import socket
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)

    #Envia uma a uma as mensagens criadas
    while True:
        for msg in LIST:
            tcp.send(msg)
            response = tcp.recv(8)
            print msg, response
            if not response:
                break
        tcp.shutdown(socket.SHUT_RDWR)  # Fecha a conexão para envio
        tcp.close()
        break


HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
if len(sys.argv) == 3:
    MESSAGES = int(sys.argv[1])  # Numero de mensagens a ser enviado
    SIZE = int(sys.argv[2])  # Tamanho de cada mensagem
    LIST = create_messages(MESSAGES, SIZE)

    f = open('./resultp2-'+sys.argv[1]+'-'+sys.argv[2]+'.txt', 'w')
    t = timeit.Timer(client)

    exectime = t.repeat(4, 10)
    for item in exectime:
        print>>f, item
    print >> f, "--"
    print >> f, "mean: ", numpy.mean(exectime)
    f.close()
else:
    print "Usage: client.py <# MESSAGES> <MESSAGES SIZE>"
    sys.exit()
