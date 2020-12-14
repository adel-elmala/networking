from socket import *
import sys
import re
if len(sys.argv) <= 1:
    
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server]')
    
    # sys.exit(2)



# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Fill in start.
tcpSerPort = 1205
tcpSerIp = 'localhost'
# tcpSerIp = sys.argv[-1]
print(tcpSerIp)
# print(type(tcpSerIp))
tcpSerSock.bind((tcpSerIp,tcpSerPort))
tcpSerSock.listen(1)

# Fill in end.
print('--- Ready to serve... ----')

while 1:
    
    # Strat receiving data from the client
    tcpCliSock, addr = tcpSerSock.accept()
    print(f'**** Received a connection from: {addr} ****')
    
    message = tcpCliSock.recv(1024).decode()    # Fill in start.       #Fill in end
    
    # print(f'message is: {message}')
    
    # Extract the filename from the given message
    # print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(f'Requisted filename is: {filename}')
    
    fileExist = False
    filetouse = "/" + filename
    # print(filetouse)
    
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = True
        # ProxyServer finds a cache hit and generates a response message
        statusLine = "HTTP/1.0 200 OK\r\n"
        tcpCliSock.send(statusLine.encode())
        headerLine = "Content-Type:text/html\r\n"
        tcpCliSock.send(headerLine.encode())
        # Fill in start.
        newLine =  "\r\n"
        tcpCliSock.send(newLine.encode())
        
        for i in range(len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
            
        # Fill in end.
        print('## Read from CACHE ##')

    # Error handling for file not found in cache
    except IOError:
        if fileExist == False:
            # Create a socket on the proxyserver
            c = socket(AF_INET,SOCK_STREAM)     # Fill in end.
            hostn = filename.replace("www.","",1)
            print(f'Hostname is: {hostn}')
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn,80))
                print(f'<-- connected to origin server {(hostn,80)} -->')
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                # fileobj = c.makefile('r', 0)
                # print('made file')
                # fileobj.write("GET  "+"http://"+ filename + "HTTP/1.0\n\n")
                getRequest = "GET "+"http://"+ filename + " HTTP/1.0\n\n"
                c.send(getRequest.encode())
                
                # Read the response into buffer
                # Fill in start.
                originSerResponse = c.recv(2048).decode()
                
                print('------------')
                # print('Received response from origin server')
                print(f'Origin response is :')
                print(originSerResponse)
                print('------------')
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                # Fill in start.
                tcpCliSock.send(originSerResponse.encode())
                with open("./" + filename,"w") as writer:
                    output = re.split(r'(\r\n\r\n)',originSerResponse)
                    print(output)
                    startData = False
                    for i in range(len(output)):
                           
                        startData = True if output[i] == '\r\n\r\n' else startData
                        if startData:
                            writer.write(output[i])
                            
                c.close()
                # Fill in end.
            except Exception as exp:
                print(exp)
                print("Illegal request")


        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n")
            # Fill in end.
            
    
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
sys.exit()
# Fill in end.