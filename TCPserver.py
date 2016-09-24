#!/usr/bin/env python
import random
from socket import *
serverPort = 12004
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# CONSTANTS ================================================================
SOLUTION_FILE = "tops95.txt"
NEW_GAME_FILE = "top95.txt"
with open(NEW_GAME_FILE, 'r') as top:
    newGame = [x.strip('\n') for x in top.readlines()]
with open(SOLUTION_FILE, 'r') as tops:
    sol = [s.strip('\n') for s in tops.readlines()]

#FUNCTION DEFINITIONS ======================================================

# CLIENT-SERVER COMMUNICATION FUNCTIONS ====================================
#Logic to find out what message was sent
def handleMsg(msg):
	print("Inside handleMsg")
	row = 0
	modifiedMessage = ""
	if (msg[0]=="1"):
		print("handleMessage if 1")
        	if(msg[1]=="0"):
			print("handleMsg if 2")
            		row = random.randint(1,95)
        	else:
			print("else")
            		row = msg[1]
	        return ( msg[0] + "::" + str(row) + "::" + newGame[int(row)-1])
    	elif(msg[0]=="2" and msg[1] == "1"):
		print("msg[0]==2 and msg[1] == 1")
		return(msg[0]+"::"+msg[1]+"::"+msg[2]+"::" + checkMove(msg[2],msg[3]))
    	elif (msg[0]=="2" and msg[1] == "2"):
        	print("Im inside get hint else")
        	return (msg[0] + "::" + msg[1]+ "::" + msg[2] + "::" + getHint(int(msg[2]),msg[3]))
	elif (msg[0] =="2" and msg[1] == "3"):
		print("i am inside solution")
		return(msg[0] + "::"+ msg[1] +"::"+ msg[2] +"::"+ sol[int(msg[2])-1])
		
    	else:
        	return("Something went wrong")
	
    	print("did not reconize flag")

def checkMove(number,game):
	count = 0
	msg =[]
	solution = sol[int(number)-1]
	print("inside check move")
	for n in game:
		if(n != solution[count] and n != "."):
			row = int(count /9)
			col = count % 9
			msg.append (str(row) + str(col))
		count +=1
	if not msg:
		return '0'
	else:
		return ''.join(msg)
		

def getHint(number, game):
	print("inside get hint method")
	count = 0
	solution = sol[number-1]
	print("solution: " + solution)
	pos = []
	for n in game:
		if(game[count] == "."):
			pos.append(count)
		count += 1
	size = len(pos)
	num = random.choice(pos)
	print("index: " + str(num))
	print("the hint: " + solution[num])
	ans = (game[:num] + solution[num] + game[(num +1):])
	print("This is from gethint method: " + ans)
	return ans



# PROGRAM ==================================================================
print("The server is ready to receive")


while 1:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print(message)
	msg = message.split('::')
	print(msg)
	modifiedMessage = handleMsg(msg)
	print("This is what I am sending: " + modifiedMessage)
	#serverSocket.sendto(modifiedMessage, cliientAddress)
        connectionSocket.send(modifiedMessage)
	connectionSocket.close()
