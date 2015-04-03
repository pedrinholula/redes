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

tcp.send(""+MESSAGES)  # Envia o tamanho da mensagem
reponse = tcp.recv(8)
if response is True:
    for x in range(MESSAGES):
        while response is True:
            msg = random.choice(string.ascii_letters)
            tcp.send(msg)
            response = tcp.recv(8)


#Conecta com o servidor @TODO
#Envia o tamanho da mensagem @TODO
#Serivdor avisa que está pronto @TODO
#Se o servidor está pronto @TODO
    #Envia uma mensagem
    #Se o servidor responde
