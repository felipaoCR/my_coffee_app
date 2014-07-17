#!/usr/bin/python

import sys
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

twilio_id = 'AC84680652a2e3a197af7ac005adbd96f0'

twilio_auth_token ='2c9cb5aed79c8854db7c7cb988a84479' 

my_phone_number = '+50683058156'

twilio_number = '+17865742721'

def sendSMS():

	try:
		client = TwilioRestClient(twilio_id, twilio_auth_token)
		message = client.sms.messages.create(body = "Making coffee ...",to =my_phone_number, from_=twilio_number)
		print "Mensaje enviado"
	except TwilioRestException as e:
		print "Couldn't send message: %s" % e
		sys.exit(0)
