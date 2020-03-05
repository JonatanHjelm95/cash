import socket


#AF_INET for IPv4, SOCK_STREAM for TCP (as opposed to UDP).
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket what IP and port number to connect to (must be in two brackets because it needs a tuple).
clientsocket.connect(('pwctf.dk', 19937))

#Recieve 1024 bytes of data.
data = clientsocket.recv(2000)

#Split the recieved data by newlines (returns a list).
data = data.split('\n')
dataSplit = data[len(data)-1].split(' ')


#The first and second elements in our list should be the two numbers we need to add together, so we do that.
result = dataSplit[0]

#Send our result to the server.
clientsocket.send('123')

#Recieve any response from the server and print it to the screen.
#data = clientsocket.recv(1024)
print(data)