import time as t
import twitter
import serial
import warnings

duinoPort = "The port in which your system will establish serial connection with Arduino" #Usually in the /dev directory in Linux

API1 = 'Your API key'

API2 = 'Your API secret'

AC1 = 'Your access token'

AC2 = 'Your access token secret'

api = twitter.Api(API1,API2,AC1,AC2)

def updateInstruction():
	
	try:
		timeline = api.GetUserTimeline("put your twitter id number")
		inst = [u.text for u in timeline][0]
		return inst
	except KeyboardInterrupt as e:
		print "Error : %s" %e
			


def main():
	flag = True
	print "Waiting for instructions ..."
	while True:
		instruction = updateInstruction()
		
		
		if instruction != "I want some coffee":

			continue
			
		else:
			print "Making coffee ..."
		
			arduino = serial.Serial(duinoPort,9600)
			msg.sendSMS("Making coffee ...")

			while flag:
				try:
					arduino.write('1')
					instruction = updateInstruction()
					t.sleep(1)
					if instruction == "Maybe I don´t want coffee":
						print "Application will now exit ..."
						arduino.close()
						msg.sendSMS("The coffee app has stopped ...")	
						flag = False
						break
					else:
						continue
				except KeyboardInterrupt:
					print "Application will now exit ..."
					arduino.close()
					break	
		if flag == False:
			break

if __name__ == "__main__":
	main()

