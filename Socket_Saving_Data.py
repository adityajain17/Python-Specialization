import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
c=0
picture = b""
while True:
    data = mysock.recv(512)
    c=c+1
    if len(data) < 1:
        break
    print(data.decode(),end='')
    picture=picture+data
mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.txt", "wt")
fhand.write(picture.decode())
fhand.close()
