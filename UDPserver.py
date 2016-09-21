#!/usr/bin/env python
import random
from socket import *
serverPort = 12004
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# CONSTANTS ================================================================
SOLUTION_FILE = "tops95.txt"
NEW_GAME_FILE = "top95.txt"


#FUNCTION DEFINITIONS ======================================================

# CLIENT-SERVER COMMUNICATION FUNCTIONS ====================================
#Logic to find out what message was sent
def handleMsg(msg):
	with open(NEW_GAME_FILE,'r') as top:
		newGame = [x.strip('\n') for x in top.readlines()]
	with open(SOLUTION_FILE,'r') as tops:
		sol = [s.strip('\n') for s in tops.readlines()]
	row = 0
	
    if (msg[0]==1):
		if(msg[1]==0):
			print("New game random")
            row = random.randint(1,95)
        else:
			print("new game 1-95")
            row = msg[1]
	modifiedMessage = msg[0] + "::" + msg[1] + "::" + newGame[row]
	elif (msg[0]==2 and msg[1] == 1):
		print("check move")
		modifedMessage = (msg[0]+"::"+msg[1]+"::"+msg[2]+"::" + checkMove(NewGame[msg[3]],sol))
	elif (msg[0]==2 and msg[1] ==2):
		print("Get Hint")
		modifedMessage = (msg[0] + "::" + msg[1]+ "::" + msg[2] + "::" + getHint(newGame[msg[2]], sol))
		print("Get Hint: " + modifiedMessage)
	return (modifiedMessage.strip())

def checkMove(moves, solution):
	count = 0
	msg
	print("inside check move")
	for n in moves:
		if(n != solution[count]):
			row = int(count /9)
			col = count % 9
			msg += (str(row) + str(col)+ " ")
		else:
			msg = 0
		count += 1
	return msge

def getHint(game,sol):
	print("inside get hint")
	count = 0
	pos = []
	for n in game:
		if(game[count] == "."):
			pos.append(count)
		count += 1
	size = len(pos)
	num = random.choice(pos)
	anwser = (game[:num] + sol[num] + game[num +1])   
	return anwser

# PROGRAM ==================================================================
print "The server is ready to receive"


while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print(message)
	msg = message.split('::')
	print(msg)
	modifiedMessage =handleMsg(msg)
	
	serverSocket.sendto(modifiedMessage, clientAddress)
