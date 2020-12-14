import socket

serverPort = 1200

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
serverSocket.bind(('', serverPort))

socketState = True
print("The server is ready to receive")

while socketState:
   
    print("---- WAITING... ----")
    message, clientAddress = serverSocket.recvfrom(2048)
    
    print(f"RECEIVIED FROM: {clientAddress}")
    print(f"RECEIVIED DATA: {message}")
    message = message.decode()
    
    if message == 'close':
        print("---- BYE ----")
        socketState = False
        serverSocket.close()
    else:
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        print("---- SENT ----")

print("---- CLOSED SUCCESSFULLY ----")
