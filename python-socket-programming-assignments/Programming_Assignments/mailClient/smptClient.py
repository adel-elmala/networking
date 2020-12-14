from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# mailServer = 'smtp.gmail.com'   #Fill in start    #Fill in end
# mailPort = 587
mailServer = 'smtp.aol.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
print('client socket created')
clientSocket.connect((mailServer,mailPort)) 
print(f'Established connection with : {(mailServer,mailPort)}')
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.

heloCommand = 'HELO Adel\r\n'

clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

print('--- SMTP handShake complete ---')



####
# """ ssl commands """
# authCommand = 'AUTH LOGIN'
# clientSocket.send(authCommand.encode())

# sslReplay = clientSocket.recv(1024).decode()
# if sslReplay.split()[0] != '334':
#     print('ssl auth login went WRONG!')

## continue later


####

# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM: <Adel-refat@Adel>'
clientSocket.send(fromCommand.encode())

recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '250':
    print('250 reply not received from server.')
print(recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
toCommand = 'RCPT TO: <adel.elmala2020@aol.com>'
clientSocket.send(toCommand.encode())
recv3 = clientSocket.recv(1024).decode()
if recv3[:3] != '250':
    print('250 reply not received from server.')
print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
if recv4[:3] != '354':
    print('354 reply not received from server.')
print(recv4)
# Fill in end

# Send message data.
# Fill in start
# data = 'SUB DUDE'
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
# period = '\r\n.\r\n'
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
if recv5[:3] != '250':
    print('250 reply not received from server.')
print(recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
if recv6[:3] != '221':
    print('221 reply not received from server.')
print(recv6)

# Fill in end