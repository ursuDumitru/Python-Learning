import socket

# an internet socket that uses TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555)) # this is the socket that we want our socket to run on
s.listen() # constantly listening to possible clients

while True:
    client, address = s.accept() # when something tries to connect to our socket
    print("Connected to {}".format(address))
    client.send("You are connected".encode())
    client.close() # we have to close it so that there won't remain zombie clients