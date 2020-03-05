import sys
import pyperclip

cashArr = [[0, 1000], [0, 500], [0, 200], [0, 100], [0, 50], [0, 20], [0, 10], [0, 5], [0, 2], [0, 1]]

amount = sys.argv[1]
dir = sys.argv[2]


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
if str(dir) == 'f':
	pyperclip.copy(str(cashArr))
if str(dir) == 'r':
	pyperclip.copy(str(list(reversed(cashArr))))
#print(cashArr)
#print(list(reversed(cashArr)))
#pyperclip.copy(str(cashArr))

dump:
		cmdLineSplit = data3.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data4 = clientsocket.recv(1024)
		print(data4)

		cmdLineSplit = data4.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data5 = clientsocket.recv(1024)
		print(data5)

		cmdLineSplit = data5.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data6 = clientsocket.recv(1024)
		print(data6)


		cmdLineSplit = data6.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data7 = clientsocket.recv(1024)
		print(data7)

		cmdLineSplit = data7.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data8 = clientsocket.recv(1024)
		print(data8)

		cmdLineSplit = data8.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data9 = clientsocket.recv(1024)
		print(data9)

		cmdLineSplit = data9.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data10 = clientsocket.recv(1024)
		print(data10)

		cmdLineSplit = data10.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data11 = clientsocket.recv(1024)
		print(data11)

		cmdLineSplit = data11.split(' ')
		for i in range(0, len(cmdLineSplit)):
			if str(cmdLineSplit[i]) == 'return':
				amount = cmdLineSplit[i+1]
			if str(cmdLineSplit[i]) == 'of':
				direction = cmdLineSplit[i+1]
		output = str(getCash(amount, direction))
		print(output)
		clientsocket.send(output+ '\n')
		time.sleep(1)
		data12 = clientsocket.recv(1024)
		print(data12)