import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("Server is listening...")

while True:

    conn, addr = server.accept()
    print('Got connection from', addr)

    # send connetion info message to the client.
    conn.send('[ACTIVE CONNECTIONS] : You are now connected!'.encode(FORMAT))

    # Message recived fron clint side
    print(conn.recv(13).decode(FORMAT))

    break

# Close the connection with the client
conn.close()
print("[SERVER] Connection Closed!")
