# coding: utf-8

import socket

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
response = bytearray(1)
print "Servidor iniciado. Aguardando conexão"
# Execução infinita
while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    while True:
        #Espera a mensagem do cliente
        msg = con.recv(1024)
        print msg
        if not msg:
            con.send(response)  # envia a ultima mensagem
            #fecha conexão para novas mensagens
            con.shutdown(socket.SHUT_RDWR)
            con.close()
            break
