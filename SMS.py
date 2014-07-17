#!/usr/bin/python

import sys
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

twilio_id = 'Your twilio API id'

twilio_auth_token ='Your twilio authorization token' 

my_phone_number = 'Your phone number (extension included)'

twilio_number = 'Your twilio number (the one with a plus sign)'

def sendSMS():

	try:
		client = TwilioRestClient(twilio_id, twilio_auth_token)
		message = client.sms.messages.create(body = "Making coffee ...",to =my_phone_number, from_=twilio_number)
		print "Mensaje enviado"
	except TwilioRestException as e:
		print "Couldn't send message: %s" % e
		sys.exit(0)
