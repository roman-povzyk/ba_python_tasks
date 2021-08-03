# During the lesson, we have created a server and client,
# which use TCP/IP protocol for communication via sockets.
# In this task, you have to create a server and client,
# which will use user datagram protocol (UDP) for communication.


import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming datagrams
while True:
    print('waiting for a connection')

    data = sock.recvfrom(1024)
    message = data[0]
    address = data[1]

    print(f'message from Client: {message}. IP: {address}')

    sock.sendto(message.upper(), address)
