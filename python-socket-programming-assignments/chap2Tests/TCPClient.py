import socket

serverIp = '192.168.1.3'
serverPort = 1205

# create a tcp socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(f'--- Created socket ---')

# initiate three-way tcp handshake with the server 
clientSocket.connect((serverIp,serverPort))
print(f'Connected to server: {(serverIp,serverPort)}')

# user input 
message = input('your input is: ')

clientSocket.send(message.encode())
print(f'Sent: {message}')

modifiedMessage = clientSocket.recv(1024)

print(f'Recived: {modifiedMessage}')

clientSocket.close()

print('--- BYE ---')
