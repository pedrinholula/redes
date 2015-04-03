import socket
HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente
    while True:
        msg_size = con.rcv(1024)
        for x in range(int(msg_size)):
            msg = con.recv(1024)
            resp = '' + x
            con.send(resp)
        print 'Finalizando conexao do cliente', cliente
        con.send("0")
        break
    con.close()
