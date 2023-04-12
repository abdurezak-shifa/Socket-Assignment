import socket
import random

# Create a TCP socket and start listening for incoming connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8500)
server.bind(server_address)
server.listen(1)

# advertise the server's services
print("Server is up and running on {}:{}".format(server_address[0], server_address[1]))
# Accept incoming connections from clients
while True:
    print("Waiting for client to enter what they want...")
    client, address = server.accept()
    print("Client connected:", address)


    # Receive the message from the client
    client_msg = client.recv(1024).decode('utf-8')
    clientName, clientNum = client_msg.split(",")
    print("Client Name:", clientName)
    print("Server Name: Server of John Q. Smith")

    # Pick a random number between 1 and 100
    serverNum = str(random.randint(1, 100))

    # Display the client's number, the server's number, and the sum
    print("Client Number:", clientNum)
    print("Server Number:", serverNum)
    total = int(clientNum) + int(serverNum)
    print("Sum:", total)

    # Send the server's name and number back to the client
    server_msg = "Server of John Q. Smith," + serverNum
    client.send(bytes(server_msg, 'utf-8'))

    # Check if the client's number is out of range
    if int(clientNum) < 1 or int(clientNum) > 100:
        print("Client Number is out of range")
        break

    # Close the client socket
    client.close()

# Close the server socket
server.close()