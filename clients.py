import socket

# Get the client name and integer from the user
name = input("Enter your name: ")
number = input("Enter an integer between 1 and 100: ")

# Open a TCP socket and send the message to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8500))
client.send(bytes(name + "," + number, 'utf-8'))

# Wait for the server's reply
serverReply = client.recv(1024)
serverName, serverNum = serverReply.decode('utf-8').split(",")

# Compute sum and Print the results 
print("Client Name:", name)
print("Server Name:", serverName)
print("Client Number:", number)
print("Server Number:", serverNum)
total = int(number) + int(serverNum)
print("Sum:", total)

# Closing the client socket
client.close()