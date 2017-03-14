import sys
import socket
import string
import time

HOST="irc.freenode.net"
PORT=6667

NICK="NICK AttorneyBot\r\n"
USER="USER AttorneyBot__ 8 * : AttorneyBot__\r\n"
SERV="JOIN #This_Is_Bat_Country\r\n"
CHAN="This_Is_Bat_Country"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))


s.send(NICK.encode('utf-8'))
s.send(USER.encode('utf-8'))
s.send(SERV.encode('utf-8'))

#var1=""


### MESSAGES

huntMsg1=str("Oh, Jeezuz! Did you see waht gOd just did to us??/\r\n")
huntMsg2=str("U btr be carefull. Plenty of vlutures out here. They''l pick your bones clean b4 morning.\r\n")
huntMsg3=str("no but i told him we had a Vincent Black Shadow. that scraed the piss outta him.\r\n")
huntMsg4=str("It just occurred to me that she has no witnesses. Anything she says about us is completely worthless.\r\n")
huntMsg5=str("Take off slowly, don't attract any attention. I told the cabbie to make sure she gets to the Americana.\r\n")
huntMsg6=str(" told him I had some business to take care of, but I'd be there myself in an hour and if the girl wasn't already checked in, I'd come back out here and rip his lungs out..\r\n")
huntMsg7=str(":)\r\n")
huntMsg8=str("As your attorney, I advise you to tell me where you put the goddamn mescaline.\r\n")
huntBlank=str(" \r\n")


#attMsg1=str("This is a test message FOR the Attorney.\r\n")
#attMsg2=str("Second messg wut.\r\n")
#attMsg3=str("3rd duder. Gj.\r\n")





def recvData():
	
	var1=""
	
	var1=var1+s.recv(2048).decode('utf-8')
	tempo=var1.split("\n")
	var1=tempo.pop()

	return(tempo)


def parseData(temp):
	for line in temp:
		print(line)
		line=line.rstrip()
		line=line.split()

	return(line)


def checkName(line):

	msg=""

	name=line[0].split("!")
	print(name[0])

	for words in line[3:]:
		msg+=(words + " ")

	print(name[0][1:] + msg + "\r")

	return(name)

def chat():

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg1).encode('utf-8'))
	time.sleep(9)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg2).encode('utf-8'))
	time.sleep(18)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg3).encode('utf-8'))
	time.sleep(14)

	s.send(("PRIVMSG #" + CHAN + " :" + huntBlank).encode('utf-8'))

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg4).encode('utf-8'))
	time.sleep(5)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg5).encode('utf-8'))
	time.sleep(12)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg6).encode('utf-8'))
	time.sleep(6)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg7).encode('utf-8'))
	time.sleep(5)

	s.send(("PRIVMSG #" + CHAN + " :" + huntMsg8).encode('utf-8'))
	time.sleep(5)


interupt=False


while 1:
#	var1=var1+s.recv(1024).decode('utf-8')
#	temp=var1.split("\n")
#	var1=temp.pop()

	temp=recvData()
	
	try:
		for line in temp:
			print(line)
			line=line.rstrip()
			line=line.split()

			if(line[0]=="PING"):
				s.send(("PONG " + line[1]).encode('utf-8'))

			elif(line[1]=="PRIVMSG"):
				
				msg=""

				name=line[0].split("!")
				print(name[0])

				for words in line[3:]:
					msg+=(words + " ")
				
				print(name[0][1:] + msg + "\r")

				cmd=name[0][1:] + msg + "\r"
				cmd=cmd.rstrip()
				if(cmd=="Lucy__:start"):
					chat()


#				elif(name[0][1:]=="Lucy__") and interupt==False:
#					interupt=True
#					time.sleep(100)
					#
					#
					#
					#
#					interupt=False

				
#				s.send(("PRIVMSG #Bat_Country :This is BAT COUNTRY\r\n").encode('utf-8'))

			else:
				for words in line:
					print(words + " ", end='')
				print("\r")

	except:
		print("Dammit")
		pass
