import time
from socket import socket , AF_INET , SOCK_DGRAM ,timeout ,sys

# create client UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

# socket rasies 'timeout' exception when operations fail if they cannot be completed within the timeout specified '1 sec'
clientSocket.settimeout(3.0) 

serverSocket = 12010
serverip = '192.168.1.3'

serverAddr = (serverip,serverSocket)

for i in range(1,11):
    tStart = time.time()
    ping = f'Ping {i} {tStart}'
    clientSocket.sendto(ping.encode(),serverAddr)
    try:
        pong , addr = clientSocket.recvfrom(1024)
        tEnd = time.time()
        RTT = tEnd - tStart
        print(f'{pong.decode()} -- RTT is: {RTT} Seconds')

    except timeout:
        print("Request timed out")
clientSocket.close()
sys.exit()