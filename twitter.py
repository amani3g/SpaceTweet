'''
Raspberry Pi Twitter Integration
Receives Data and Tweets It

Default twitter.py file
'''

#API KEYS

consumer_key = 
consumer_secret = 
access_token =
access_token_secret = 

from twython import Twython

from auth import(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

#Make a connection with the Twitter API using this set of keys

twitter = Twython(
	consumer_key,
	consumer_secret,
	access_toke,
	access_token_secret
	)

#Test connection
message = "Hello world!"
twitter.update_status(status = message)
print("Tweeted: %s" %message)
