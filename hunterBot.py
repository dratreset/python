import sys
import socket
import string
import time

HOST="irc.freenode.net"
PORT=6667

NICK="NICK HunterBot\r\n"
USER="USER HunterBot__ 8 * : HunterBot__\r\n"
SERV="JOIN #This_Is_Bat_Country\r\n"
CHAN="This_Is_Bat_Country"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))


s.send(NICK.encode('utf-8'))
s.send(USER.encode('utf-8'))
s.send(SERV.encode('utf-8'))

#var1=""

### MESSAGES

#huntMsg1=str("This is a test message FOR Hunter.\r\n")
#huntMsg2=str("2 Test msg.\r\n")
#huntMsg3=str("3 msg test ya.\r\n")


attMsg1=str("God didnt do that!!1 U did it! Youre a fucking narcotics agent! I wazz on 2 your stinking act fr0m teh start, you PIG!\r\n")
attMsg2=str("You whore.\r\n")
attMsg3=str("When we get to Las VEgas ill hav you chopped into hamburger. What do you think the Drug Bund will do when I show up with a Samoan narcotics agent?\r\n")
attMsg4=str("Does he understand we have magnums?\r\n")
attMsg5=str("Good, but what about our room? and the golf shoes? were right n the midddle of a fucking reptile zoo! & somebodys giving BOOZE to these goddamn things!1! It wont b long before they tear us to shreds. Jesus, lok at the floor! Have you ever seen so much blood?\r\n")
attMsg6=str("\"Us\"?\r\n")
attMsg7=str("You think she will??\r\n")
attMsg8=str("That's good, can't b subtlr in this town.\r\n")
attBlank=str(" \r\n")

ascii1=str("$$$$$$$$$$$$$$$$$7$$$$$$$$$$7777$$$$$77$7$7$7$7$7777777$77$$7777$$777777777$7$77777$7$77$$$77$$$$$$7$$$$$$$$$$$$$$$$$$$$\r")
ascii2=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$7777$$$$$$777$777I77777$7IIIII77$$777777$77$7$$777777$7$$7$77$$$$$$$$$$$$$$$$$$$$$$$$$$$\r")
ascii3=str("$$$$$$$$$$$$$$$7$$$$$$$$$$77$$$7$77777$$$7$7$7IZIIIIIIIIIIIIIIIII$$77777777777$77$77$$$7$7$$7$$$$$$77$$$$$$$$$$$$$$$$$$$\r")
ascii4=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$7$$7$$$$77$$77$ZZII7IIIIIIIIIIIIIIII$777$777$777$77$77777$$7$$77$$$$$$7$$$$$$$$77$$$$$$$$$\r")
ascii5=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$$77$$7$$$77I7IIIIIIIIIIIIIIIIIIIII7777777777$77777$7$77$$$77$$$$$7$$$$$$$$$$$$$$$$$$$$\r")
ascii6=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$$$$77$$IIIIIIIIIIIIIIIIIIIIIIIIIIII7777777$77777$77777$$7$$$$$$$7$$$$$$$$$$$$$$$$$$$\r")
ascii7=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$77$II$III7IIIIIIIIIIIIIIIIIII7II77777777777$$77$7$$$$7$$$$$$$7$$$$$$$$7$$$$$$$$$$\r")
ascii8=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$77$77IZI7IIIIIII8888OZ$777777$887III777777$$777777777$7$77$$$$$$77$$$$$$$$$$$$$$$$$$\r")
ascii9=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$$7$$IZI8O77NNNNNNNNNNNNNNNNNNNNNNNNO7777I7$$77$77$$$7$$$$7$$7$$$$7$$$$$$$$$$$$$$$$$$\r")
ascii10=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$77$$887NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNO78$$$$$7777$7$7777$$$$$$$$$$$$$$$$$$$$$$$$\r")
ascii11=str("$$$$$$$$$$$$$$$$$$$$$$$$$$7$$$$$$$7887NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN7O777$7777$$$77$$$$$$$$$$$$$$$$$$$$$$$$$\r")
ascii12=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z87NNNNNNNNNNNNND888888888888$++++88DNNNNNNNNNNNN7$7$$77$$$777$$$7$$7$$$$$$$$$$$$$$$$$$\r")
ascii13=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$88NNNNNNNNN8+++++++++++++++++++,,:+++++8NNNNNNNNNNN8$77$77$$$77$$$$7$77$$$$$$$$$$$$$$$$$\r")
ascii14=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$88NNNNNNNNOOOOODDDDOO++,+++++++ZODDDDD8OO+8NNNNNNNNN77$$$77$$$77$$7$$$7$$$$$$$$77$$$$$$$$\r")
ascii15=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$7$78NNNNNNNNOOOO8DDDDDDDDO.+++++,OOOOOODDDDDOO8NNNNNNNN787$7$77$$777$7$$$7$$$$$$$$$$$$$$$$$$\r")
ascii16=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNNNOZOOOOODDDDDDDO+88O88+ZOOOOOODDDDDD+NNNNNNNN78$$7$$$$$777$$$$$$$$$$$$$$$$$$$$$$$$\r")
ascii17=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$78NNNNNNNOZOOOOOOODDDDDO+7777O+ZOOOZZOOOOOOO7NNNNNNNNZ8$777777$$77$77$$$7$$$$$$$$7$$$$$$$$\r")
ascii18=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$78NNNNNNNNOZOOOOOOOOOOOO87I7777O+OZ$$$$$$$OOO+NNNNNNNNZ$7$$$77$$$77$$$7$$$$$7$$$$$$$$$$$$$$\r")
ascii19=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNNNNOOZOOOOOOOZOO7+777Z77$O+OO$$$$$$$OO+NDNNNNNN8$777$77$$$77$$7$$$7$$$$$$$$$$$$$$$$$\r")
ascii20=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNNNNN+OZZZZZZZO+Z+777Z7777OOO+OOO$$$OO?DDDDNNNNN8$777$$7$$$77$7$7$$77$$$$$$$$$$$$$$$$\r")
ascii21=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$78NNNNNNNNNN7+OOOO+++8+777Z$7I77OONOO+++??+NZDDNNNNNNN$$77$777$$$$7$$7$$$77$$$$$$$$$$$$$$$$\r")
ascii22=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNNNDDND88888888$777Z8$7II77OOONNNNOOO7ZZDDNNNNN87$$777$7$7$$77$$7$$7$$$$$$$$$$$$$$$$$\r")
ascii23=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNNNDN8D8888887777$888$IIII777OOOOOI77Z77DNNNN8$77$$7$77$$$$77$$$$$7$$$$$$$$$7$$$$$$$\r")
ascii24=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8NNNNNDND888DD887777D$NN88DDD7O8Z77777777777NNNN87$77777$$7777$77$$7$$$$$$$$$$$$$$$$$$$$\r")
ascii25=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NNNNDDD88888ZZZZZZ888O8O7777777777777777I7NNN$77$77$77$777$$$77$$$$$77$$$$$$$$$$$$$$$$\r")
ascii26=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NNNDDD888ZZZZZZZZZZ77777777777777777N77NN$7$7$$77777$77$$$$77$$$$7$7$$$$$$$$$$$$$$$$\r")
ascii27=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$NDD888OZZZZZZZ7OO7OOO777777777777$NN$77$7$77$77$777$$77$777$$$$$7$$$$$$$$$$$$$$$$\r")
ascii28=str("$$$$$$$$$$$$$$$$$$$$$$$$$$OZ7:::::::::I??:=7777777Z$88$$$788OO77777777777$77777$777$7$$777$$$7$$77$$$$$7$$$$$$$$$$$$$$$$\r")
ascii29=str("$$$$$$$$$$$$$$$$$$$$$$$$$$ZO7:::::::::?IIOOOZ7777777$77777777$$87777777777777777777$77$7777$77$777$$7$$$$$$$$$$$$$$$$$$$\r")
ascii30=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$DDDD$$$$$OOOOO777777777777777$D7777777$7$$7$$7$777$$$77$$$$$$7$$$$$$$$$$$$$$$\r")
ascii31=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8DDDD$$$$$$$$OOOO$$$$$$777777II+++O777777$77777777$$$$77$$7$$$7$$$$$$$$$$$$$$$\r")
ascii32=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8DNDDDD$$$$$$$$$$$$$$$$$$$7777II+++++O7$7$7$7$7777$$$$$$7$$$7$$7$$$$$$$$$$$$$$$\r")
ascii33=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$8D8DNDDDD$$$$$$$$$$$$$$$$$$777DDII$+++OO7777$77$777$77$$$77$$$$$$7$$$$$$$$$$$$$$\r")
ascii34=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$DDO88NNNNDDD$$$$$$$$$$$$$$$$8DDDIII++++ZOO$77$$777$7777$$$77$$$$$77$$$$$$$$$$$$$$\r")
ascii35=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$D8O888IIONNDD$$$$$$$$$$$$$NIDDIIIIII++=Z$OZ7$$$7777777$$7$77$$$7$$$$$$$$$$$$$$$$$\r")
ascii36=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ODD8DOO8888IINNNNDDDDZ$$$ODNNIIIIIIII=II+ZZZZZOO$7777$$$77$$7$77$$$$$$$$$$$$$$$$$$$$$\r")
ascii37=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$DDDD8DOO$O88888IIINNN8IIIIIIIIIIIIIIII==II$=ZZZOZ$88877777$$$$7$77$$$$$$7$$$$$$$$$$$$$$\r")
ascii38=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$IIIID8DO7$OO88888888OID8IIIIIIIIIDIIII===III=+OZZZZZ$88888Z77777$$$7$$7$$7$$$$$$$$$$$$$$$\r")
ascii39=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$IIIIIIIDO+++OOO88DD888888IIDDDDDIIIIII=====III++ZZZZZOOZ8888888777$$$77$$$$$7$$$$$$$$$$$$$$\r")
ascii40=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$I88888888D++$+OOO8D88DD88IIIIIIIIIIIIII=====IIIIO$ZZZZZ$ZZIIII88888Z$$$77$77$$7$$$$$$$7$$$$$$\r")
ascii41=str("$$$$$$$$$$$$$$$$$$$$$$$$$Z?????????D+++++Z$OZ88888DD888OIIIIIIIII======IIIIZZZOZZZZZZZNIIIII8888$$77$77$$7$$$$$$$$$$$$$$\r")
ascii42=str("$$$$$$$$$$$$$$$$$$$$$$ZI??????????8O++++++O$I8888888888D88IIIIII======IIIIINNOZZZZZZZZZZNDN$II$8887$$$$7$$$$$$$$$$$$$$$$\r")
ascii43=str("$$$$$$$$$$$$$$$$$$$$Z?????????????D++$+++++OOII8888888888888III=====IIIIIIOOONNZDDDD77777DDNN$$$$$O7$$$7$7$$$$$$$$$$$$$$\r")
ascii44=str("$$$$$$$$$$$$$$$$$$$??$???????????I+++++++++++OIII7IIIII7778888I===IIIIIIIIOOO8NNDDDD777777ZNDDN$$$$$$7$7$$$$$$$$$$$$$$$$\r")
ascii45=str("$$$$$$$$$$$$$$$$$?$$DDD??????????8+++++++++++$DDNNNNO$II7$NNNNNNNNIIIIIIIIIOOONDDDDD77777777ZNDDDN$$$$$$$77$$$$$$$$$$$$$\r")
ascii46=str("$$$$$$$$$$$$$$$$$$$$$DDDD$???????+++++++++++$+$NNZI7NNNNNNNNNNNNIIIIIIIIIIIOOODDDDDDD777777777ZDDNNDND$$$77$$$$$$$$7$$$$\r")
ascii47=str("$$$$$$$$$$$$$$$$$$$$$$$$$DDDDDDD?++$$$+++?$7++++NOONIIIIIIIIIIIIIIIIIIIIIIOOONNDDDDDD77777777777ZZDNDDND$$$$$$$$$$7$$$$$\r")
ascii48=str("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$D++++++++++++++++NOOOONNIIIIIIIIIIIIIIIIIOOOOOONDDDDDD77777777777ZZZNNDND$$$$$$7$$$$$$$$")


def recvData():

	var1=""

	var1=var1+s.recv(2048).decode('utf-8')
	tempo=var1.split("\n")
	var1=tempo.pop()

	return tempo


def parseData(temp):
	for line in temp:
		print(line)
		line=line.rstrip()
		line=line.split()

	return line


def checkName(line):

	msg=""

	name=line[0].split("!")
	print(name[0])

	for words in line[3:]:
		msg+=(words + " ")
	
	print(name[0][1:] + msg + "\r")

	return name


def asciiArt():

	interupt=True
	
	s.send(("PRIVMSG #" + CHAN + " :" + ascii1).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii2).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii3).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii4).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii5).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii6).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii7).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii8).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii9).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii10).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii11).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii12).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii13).encode('utf-8'))
	time.sleep(5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii14).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii15).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii16).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii17).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii18).encode('utf-8'))
	time.sleep(10)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii19).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii20).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii21).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii22).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii23).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii24).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii25).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii26).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii27).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii28).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii29).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii30).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii31).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii32).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii33).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii34).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii35).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii36).encode('utf-8'))
	time.sleep(10)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii37).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii38).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii39).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii40).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii41).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii42).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii43).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii44).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii45).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii46).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii47).encode('utf-8'))
	time.sleep(.5)
	s.send(("PRIVMSG #" + CHAN + " :" + ascii48).encode('utf-8'))
	#time.sleep(.5)

	interupt=False


def chat():

	time.sleep(4)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg1).encode('utf-8'))
	time.sleep(8)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg2).encode('utf-8'))
	time.sleep(2)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg3).encode('utf-8'))
	time.sleep(9)

	s.send(("PRIVMSG #" + CHAN + " :" + attBlank).encode('utf-8'))
	
	s.send(("PRIVMSG #" + CHAN + " :" + attMsg4).encode('utf-8'))
	time.sleep(11)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg5).encode('utf-8'))
	time.sleep(10)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg6).encode('utf-8'))
	time.sleep(8)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg7).encode('utf-8'))
	time.sleep(10)

	s.send(("PRIVMSG #" + CHAN + " :" + attMsg8).encode('utf-8'))
	time.sleep(5)
					
#interupt=False


while 1:
#	var1=var1+s.recv(2048).decode('utf-8')
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
				
				cmd=name[0][1:] + msg
				cmd=cmd.rstrip()
				print("Command: " + cmd)

				if(cmd=="Lucy__:start"):
					chat()

				elif(cmd=="Lucy__:ascii"):
					asciiArt()

#				if(name[0][1:]=="AttorneyBot") and interupt==False:
#					print(attMsg1)


#				elif(name[0][1:]=="Lucy__") and interupt==False:
#
#					interupt=True
#
#					
#					interupt=False

#				s.send(("PRIVMSG #Bat_Country :This is BAT COUNTRY\r\n").encode('utf-8'))

#			elif(line[6]=="/NAMES"):
#				s.send(("PRIVMSG #" + CHAN + " :Hi.\r\n").encode('utf-8'))


			else:
				for words in line:
					print(words + " ", end='')
				print("\r")

	except:
		print("Dammit")
		pass




