import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
print('Connecting to ', SERVER)
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(client.recv(45).decode(FORMAT))

# send Hello, world! message to the server.
message = 'Hello, world!'.encode(FORMAT)
client.send(message)

# Close the connection
client.close()

print("[CLIENT] Connection Closed!")
