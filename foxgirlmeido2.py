import socket
import sys

server = "chat.freenode.net"       #settings
channel = "##dakimakura"
botnick = "FoxgirlMeido"
chirp = "chirps contentedly"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth


irc.send("JOIN "+ channel +"\n")        #join the chan




while 1:    #puts it in a loop
	text=irc.recv(2040)  #receive the text
	print text   #print text to console

	if text.find('PING') != -1:                          #check if 'PING' is found
		irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)

	if text.find(":Hi FoxgirlMeido") != -1 or text.find(":Hi foxgirlmeido") != -1 or text.find(":hi foxgirlmeido") != -1 or text.find(":hi FoxgirlMeido") != -1:
		irc.send("PRIVMSG " + channel +  " :Hiiiiiii!  \n")
		
	if text.find(':!pat foxgirlmeido') != -1 or text.find(':!pat FoxgirlMeido') != -1:
		irc.send("PRIVMSG " + channel + " :\x01ACTION chirps contentedly\x01\n")

	if text.find("JOIN #") != -1:
		irc.send("PRIVMSG " + channel + " :Okaeri~ \n")
	#if text.find("!grope foxgirlmeido") != -1 or text.find("!grope Foxgirlmeido") != -1:
		#irc.send("PRIVMSG " + channel + " :\x01ACTION bites %s's hand.\x01\n") % 
