# Change your socket program 
# so that it counts the number of characters it has received 
# and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters 
# and display the count of the number of characters at the end of the document.

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

    receive = b''
    while True:
        data = mysock.recv(512)
        print(data)
        if len(data) < 1:
            break
        receive = receive + data
    receive = receive.decode()
    print(receive[:3000])
    print(len(receive))

    mysock.close()
except:
    print("The URL is an improperly formatted or non-existent URL. Please enter again: ")
