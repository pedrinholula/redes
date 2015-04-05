# coding: utf-8
import sys
import timeit


def create_messages(numM, sizeM):
    import random
    #Cria a lista de mensagens
    msg_lst = []
    for msg in range(numM):
        w = bytearray(random.getrandbits(8) for i in range(sizeM))
        msg_lst.append(w)
    return msg_lst


def client():
    import socket
    #Faz a conexão cliente servidor
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    #Envia uma a uma as mensagens criadas
    for msg in LIST:
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
    LIST = create_messages(MESSAGES, SIZE)

    f = open('./resultp1-'+sys.argv[1]+'-'+sys.argv[2]+'.txt', 'w')
    t = timeit.Timer(client)

    exectime = t.repeat(4, 10)
    for item in exectime:
        print >> f, item
    print >> f, "--"
    print >> f, "mean: ", reduce(lambda x, y: x + y, exectime) / len(exectime)
    f.close()
else:
    print "Usage: client.py <# MESSAGES> <MESSAGES SIZE>"
    sys.exit()
