import socket
msgfromclient = "Hello udp server"
bytesTosend = str.encode(msgfromclient)
severAddressPort = ('127.0.0.1', 20001)
buffersize = 1024
UDPCLIENTSOCKET=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPCLIENTSOCKET.sendto(bytesTosend, severAddressPort)
msgfromserver = UDPCLIENTSOCKET.recvfrom(buffersize)
msg = "message from server {}".format(msgfromserver[0])
print(msg)
