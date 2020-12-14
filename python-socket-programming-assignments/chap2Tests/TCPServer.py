import socket

serverPort = 1205

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
print(f'---- Created serverSocket ----')

serverSocket.listen(1)
print(f'serverSocket Listening...')

serverState = True

while serverState:
    connectionSocket , clientAddr = serverSocket.accept()
    print(f'conncted with: {clientAddr}')
    print(f'-- Created connectionSocket --')
    
    recievedMessage = connectionSocket.recv(1024).decode()
    print(f'Recived: {recievedMessage}')
    if recievedMessage == 'close':
        connectionSocket.close()
        print(f'-- End connection --')

    elif recievedMessage == 'close all':
        serverState = False

    else:

        modifiedMessage = recievedMessage.upper()
        connectionSocket.send(modifiedMessage.encode())
        
        print(f'Sent: {modifiedMessage}')
        connectionSocket.close()
        print(f'-- End connection --')

serverSocket.close()
print(f'---- SERVER is CLOSED ----')
