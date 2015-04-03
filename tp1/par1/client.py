import socket
import random
import string

HOST = '10.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

tcp.send("1000")  # Envia o tamanho da mensagem TODO
for x in range(1000):
    msg = random.choice(string.ascii_letters)
    tcp.send(msg)
    response = tcp.recv(1024)
    print msg, response
response = tcp.recv(1024)
print response
tcp.close()
