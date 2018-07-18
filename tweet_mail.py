'''
Tweets Data Received From Gmail

-Amani Garvin
'''
import twitter as tw
import get_gmail_data as ggd

#Loop: When New Mail Get Email Body

#Get Data from Gmail
mail_data = ggd.get_email_body()
data_parsed = ggd.parsed_email()

#Make It Into A Tweet
tweet = "Hello Earth!"


for data in data_parsed:
    tweet += "data"

#Tweet It
tw.tweet_message(tweet)





