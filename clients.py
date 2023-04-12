import socket

# Get the client name and integer from the user
name = input("Enter your name: ")
num = input("Enter an integer between 1 and 100: ")

# Open a TCP socket and send the message to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.5.232.129', 8000))
client_socket.send(bytes(name + "," + num, 'utf-8'))

# Wait for the server's reply
server_reply = client_socket.recv(1024)
server_name, server_num = server_reply.decode('utf-8').split(",")

# Compute sum and Print the results 
print("Client Name:", name)
print("Server Name:", server_name)
print("Client Number:", num)
print("Server Number:", server_num)
sum = int(num) + int(server_num)
print("Sum:", sum)

# Closing the client socket
client_socket.close()