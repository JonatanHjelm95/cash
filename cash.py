import os
import sys
import subprocess
from subprocess import Popen, PIPE
import socket
import time
import nclib

def getCash(amount, direction):
	cashArr = [[0, 1000], [0, 500], [0, 200], [0, 100], [0, 50], [0, 20], [0, 10], [0, 5], [0, 2], [0, 1]]
	for i in range(0, len(str(amount))):
		amount = str(amount)
		if len(str(amount)) == 3:
			if i == 0:
				if int(amount[i]) == 9:
					cashArr[1][0] = 1
					cashArr[2][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 7:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
				if int(amount[i]) == 6:
					cashArr[1][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 5:
					cashArr[1][0] = 1
				if int(amount[i]) == 4:
					cashArr[2][0] = 2
				if int(amount[i]) == 3:
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 2:
					cashArr[2][0] = 1
				if int(amount[i]) == 1:
					cashArr[3][0] = 1
			if i == 1:
				if int(amount[i]) == 9:
					cashArr[4][0] = 1
					cashArr[5][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 7:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
				if int(amount[i]) == 6:
					cashArr[4][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 5:
					cashArr[4][0] = 1
				if int(amount[i]) == 4:
					cashArr[5][0] = 2
				if int(amount[i]) == 3:
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 2:
					cashArr[5][0] = 1
				if int(amount[i]) == 1:
					cashArr[6][0] = 1
			if i == 2:
				if int(amount[i]) == 9:
					cashArr[7][0] = 1
					cashArr[8][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 7:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
				if int(amount[i]) == 6:
					cashArr[7][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 5:
					cashArr[7][0] = 1
				if int(amount[i]) == 4:
					cashArr[8][0] = 2
				if int(amount[i]) == 3:
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 2:
					cashArr[8][0] = 1
				if int(amount[i]) == 1:
					cashArr[9][0] = 1


		if len(str(amount)) == 4:
			if i == 0:
				cashArr[0][0] = int(amount[i])
			if i == 1:
				if int(amount[i]) == 9:
					cashArr[1][0] = 1
					cashArr[2][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 7:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
				if int(amount[i]) == 6:
					cashArr[1][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 5:
					cashArr[1][0] = 1
				if int(amount[i]) == 4:
					cashArr[2][0] = 2
				if int(amount[i]) == 3:
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 2:
					cashArr[2][0] = 1
				if int(amount[i]) == 1:
					cashArr[3][0] = 1
			if i == 2:
				if int(amount[i]) == 9:
					cashArr[4][0] = 1
					cashArr[5][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 7:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
				if int(amount[i]) == 6:
					cashArr[4][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 5:
					cashArr[4][0] = 1
				if int(amount[i]) == 4:
					cashArr[5][0] = 2
				if int(amount[i]) == 3:
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 2:
					cashArr[5][0] = 1
				if int(amount[i]) == 1:
					cashArr[6][0] = 1
			if i == 3:
				if int(amount[i]) == 9:
					cashArr[7][0] = 1
					cashArr[8][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 7:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
				if int(amount[i]) == 6:
					cashArr[7][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 5:
					cashArr[7][0] = 1
				if int(amount[i]) == 4:
					cashArr[8][0] = 2
				if int(amount[i]) == 3:
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 2:
					cashArr[8][0] = 1
				if int(amount[i]) == 1:
					cashArr[9][0] = 1

		if len(str(amount)) == 5:
			if i == 0:
				am = amount[0]+amount[1]
				cashArr[0][0] = int(am)
			if i == 2:
				if int(amount[i]) == 9:
					cashArr[1][0] = 1
					cashArr[2][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 7:
					cashArr[1][0] = 1
					cashArr[2][0] = 1
				if int(amount[i]) == 6:
					cashArr[1][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 5:
					cashArr[1][0] = 1
				if int(amount[i]) == 4:
					cashArr[2][0] = 2
				if int(amount[i]) == 3:
					cashArr[2][0] = 1
					cashArr[3][0] = 1
				if int(amount[i]) == 2:
					cashArr[2][0] = 1
				if int(amount[i]) == 1:
					cashArr[3][0] = 1
			if i == 3:
				if int(amount[i]) == 9:
					cashArr[4][0] = 1
					cashArr[5][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 7:
					cashArr[4][0] = 1
					cashArr[5][0] = 1
				if int(amount[i]) == 6:
					cashArr[4][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 5:
					cashArr[4][0] = 1
				if int(amount[i]) == 4:
					cashArr[5][0] = 2
				if int(amount[i]) == 3:
					cashArr[5][0] = 1
					cashArr[6][0] = 1
				if int(amount[i]) == 2:
					cashArr[5][0] = 1
				if int(amount[i]) == 1:
					cashArr[6][0] = 1
			if i == 4:
				if int(amount[i]) == 9:
					cashArr[7][0] = 1
					cashArr[8][0] = 2
				# change maybe
				if int(amount[i]) == 8:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 7:
					cashArr[7][0] = 1
					cashArr[8][0] = 1
				if int(amount[i]) == 6:
					cashArr[7][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 5:
					cashArr[7][0] = 1
				if int(amount[i]) == 4:
					cashArr[8][0] = 2
				if int(amount[i]) == 3:
					cashArr[8][0] = 1
					cashArr[9][0] = 1
				if int(amount[i]) == 2:
					cashArr[8][0] = 1
				if int(amount[i]) == 1:
					cashArr[9][0] = 1
	if str(direction) == "lowest":
		return list(reversed(cashArr))
	else:
		return cashArr

def processMethod():
	p = subprocess.Popen(["nc pwctf.dk 19937"], stdout=subprocess.PIPE, shell=True)
	output = list(p.stdout)
	cashAmount = ''
	direction = ''
	print(p.communicate()[0])
	for i in range(0, len(output)):
		#print(output)
		if i == int(len(output)-2):
			splitted = str(output[i]).split(' ')
			for j in range(0, len(splitted)):
				if splitted[j] == 'return':
					cashAmount = splitted[j+1]
				if splitted[j] == 'of':
					direction = splitted[j+1]
	print(getCash(cashAmount, direction))
	p.communicate(str(getCash(cashAmount, direction)))
			#print('line: ', output[i])

def socketMethod():
	amount = ''
	direction = ''
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('pwctf.dk', 19937))
	#clientsocket.shutdown(socket.SHUT_WR)
	i = 0
	while i < 20:
		d = i
		p = i
		try:
			time.sleep(1)
			data = clientsocket.recv(1024)
			dataSplit = data.split('\n')
			cmdLine = dataSplit[12]
			cmdLineSplit = cmdLine.split(' ')
			for i in range(0, len(cmdLineSplit)):
				if str(cmdLineSplit[i]) == 'return':
					amount = cmdLineSplit[i+1]
				if str(cmdLineSplit[i]) == 'of':
					direction = cmdLineSplit[i+1]
			output = str(getCash(amount, direction))
			clientsocket.send(output+ '\n')
			time.sleep(1)
		except:
			pass
		
		d = clientsocket.recv(1024)
		print(d)
		cmdLineSplit = d.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		p = clientsocket.recv(1024)
		print(p)

		i+=1
	clientsocket.close()


def socketMethod2():
	amount = ''
	direction = ''
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	x = s.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
	s.connect(('pwctf.dk', 19937))
	while x == 0:
		x = s.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 0)
		rcvdData = s.recv(1024)
		print(rcvdData)
		time.sleep(1)
		s.send('output'+ '\n')
		time.sleep(1)
		rcvdData = s.recv(1024)
		print(rcvdData)
	#clientsocket.shutdown(socket.SHUT_WR)
	#time.sleep(1)
	#clientsocket.send('1234')
	#print(clientsocket.recv(1024))

	s.close()



if __name__ == '__main__':
	socketMethod()

