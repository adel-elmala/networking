# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import sys

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12010))
serverStatus = True
while serverStatus:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print(f'Recived -- {message.decode()} -- from {address}')
    
    # Capitalize the message from the client
    message = message.upper()
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        print('dropped')
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
    if message.decode().split()[1] == '10':
        serverStatus = False
        print('end')

serverSocket.close()
sys.exit()