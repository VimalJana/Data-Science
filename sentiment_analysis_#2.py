import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'C3aSDinduwQTTh2pC7y07q6tg'
consumer_secret= 'KI0suQmRq7P9EhvcLglTgt818rz5bdU8J5n2Kr13OWIqvQBtGb'

access_token='1867499838-KK506izANg8sU5zArd69gr1RojVADZLbasJdnUt'
access_token_secret='UQ1YKmSC1eKYKLxDD8EDMrYUrOmFy81aoRTib3v6MRQR6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Machine Learning')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
