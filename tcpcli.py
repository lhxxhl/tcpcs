import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #网络 TCP

s.connect(('127.0.0.1',8082))

print (s.recv(1024))

for data in [b'data1',b'data2',b'data3']:
    s.send(data)
    print (s.recv(1024))

s.send(b'exit')
s.close()
