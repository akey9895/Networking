import socket
'''Implementation of a basic server that receives at most one connection from an incoming client'''
port=8888
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Sets up options for the socket, in this case the local address is allowed to be reused
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#sets up the address for servr to bind to and be hosted on
address=('',port)
server.bind(address)

#The server will only receive at most  1 connection
server.listen(1)

print "Now serving a HTTP connectio on %s" %port


'''Starts the server for connection by incoming clients and
sends a message  to the client once connection is established '''

while 1:
    client_connection,client_addr=server.accept()
    request=client_connection.recv(1024)
    print request

    response="Hello, thank you for you for connecting to my server"
    client_connection.sendall(response)
    client_connection.close()

