import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# The data, encrypted using the Caesar cipher algorithm
server_text = 'ATTACKATONCE'


# Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            client_key_str = str(data.decode())
            client_key_int = int(client_key_str)
            print(f'client key — {client_key_int}.')
            if data:
                print('sending data back to the client')
                print(encrypt(server_text, client_key_int))
                connection.sendall(str.encode(encrypt(server_text, client_key_int)))
                break
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
