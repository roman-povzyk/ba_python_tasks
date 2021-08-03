import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a UDP socket at client side
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Send to server using created UDP socket
    s.sendto(b'Hello, world', (HOST, PORT))
    data = s.recvfrom(1024)

print('Received from server', repr(data))
