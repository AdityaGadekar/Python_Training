import socket
localIP = '127.0.0.1'
localport = 20001
bufferSize = 1024
msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

UDPSERVERSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPSERVERSOCKET.bind((localIP,localport))
print("UDP server up and listening...")
while True:
    bytesAddresspair = UDPSERVERSOCKET.recvfrom(bufferSize)
    message = bytesAddresspair[0]
    address = bytesAddresspair[1]

    clientmsg = "Message from client{}".format(message)
    ClientIP = "Client IP address:{}".format(address)

    print(clientmsg)
    print(ClientIP)
    UDPSERVERSOCKET.sendto(bytesToSend, address)
