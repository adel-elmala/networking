#import socket module
from socket import socket , AF_INET , SOCK_STREAM,gethostname

import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)


#Prepare a sever socket


#Fill in start
serverPort = 1201
serverSocket.bind(('',serverPort))
# print(f'Server Welcome socket bind to {(gethostname(),serverPort)}') 
serverSocket.listen(1)

ServerState = True
#Fill in end
print('--- Ready to Serve... ---')

while ServerState:

    #Establish the connection

    connectionSocket, addr =   serverSocket.accept() #Fill in start      #Fill in end
    print(f'--- Connected to: {addr} ---')
    
    try:
        message = connectionSocket.recv(1024).decode()  #Fill in start    #Fill in end
        # print(f'http Request: {message}')
        filename = message.split()[1]   # separator is 'space'
        print(f'Request file: {filename}')
        if filename == '/close':
            # To close server 
            ServerState = False
            print(f'ServerState: {ServerState}')
            connectionSocket.close()

        else:
            #Fill in start    
            with open(filename[1:],'r') as reader:
                outputdata = reader.readlines() 
            #Fill in end
        
            #Send one HTTP header line into socket
            #Fill in start
            statusLine = 'HTTP/1.1 200 OK\r\n'
            connectionSocket.send(statusLine.encode())
            #Fill in end
        
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
            print('Sent')
            print('-- Connection closed --')

    except IOError:
        #Send response message for file not found
        
        print('Request page is not found')
        #Fill in start
        statusLine = 'HTTP/1.1 404 Not Found\r\n'
        connectionSocket.send(statusLine.encode())
        #Fill in end
        
        #Close client socket
        
        #Fill in start
        connectionSocket.close()
        print('-- Connection closed --')

        #Fill in end
serverSocket.close()
print('-- Server closed --')

sys.exit()#Terminate the program after sending the corresponding data