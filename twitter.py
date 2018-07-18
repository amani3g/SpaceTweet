'''
Twitter Integration
Receives Data and Tweets It 

Default twitter.py file
Run with Python3 on this machine!
Using Python Version 3
'''

#API KEYS

consumer_key = 'Ebi0vb3E5KI8SdONXSyF5EY5U'
consumer_secret = 'tSrz65e9hcuRgOA69AvD9fCVaJyBp0pYLfgF24aDugVeTw95Z5'
access_token = '1018998850147643393-SeoW4o8EOKY6T2miKCIhyJ7jpJKXRT'
access_token_secret = 'zNLpI36cYwJWI47JjTHIttnyWti8p7Mh6K7u65LW3KvYy'

from twython import Twython

#Make a connection with the Twitter API using this set of keys
twitter = Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
	)

#Test Connection
#message =  #get message from email!
#twitter.update_status(status = message)
#print("Tweeted: %s" %message)

def tweet_message(message):
    twitter.update_status(status = message)
    print("Tweeted: %s" %message)

    return

#Testing Function
#message = "Making some new functions right now!"
#tweet_message(message)
