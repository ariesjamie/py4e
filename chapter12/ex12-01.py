import socket

#url = http://data.pr4e.org/romeo.txt
try:
    url = input("Please enter a website url: ") 
    words = url.split('/')
    hostname = words[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((hostname, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print("The URL is an improperly formatted or non-existent URL. Please enter again: ")
