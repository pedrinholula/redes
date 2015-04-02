import socket
HOST = '10.0.0.1' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
ba = bytearray(1000)
for msg in ba:
    while reponse <> '0':
        tcp.send (msg)
        response = tcp.recv(1024)
tcp.close()
