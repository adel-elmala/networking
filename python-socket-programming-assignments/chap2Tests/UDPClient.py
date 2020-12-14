import socket  
import PIL
serverName = 'adel-Inspiron-N5110'
serverIp = '127.0.1.1'
# serverIp = '172.18.0.27' # to Repl.it
serverPort = 1200

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input lowercase sentence: ')

if message != 'close':

    clientSocket.sendto(message.encode(),(serverIp, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(f'Recived message: {modifiedMessage.decode()}')
    print(f'server address is: {serverAddress}')

else:
    clientSocket.sendto(message.encode(),(serverIp, serverPort))


clientSocket.close()