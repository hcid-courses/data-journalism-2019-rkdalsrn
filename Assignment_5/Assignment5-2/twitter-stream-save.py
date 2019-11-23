import tweepy
import json

consumer_key = 'cVsAwDkjs83ZBM5dyOBUNTaUd'
consumer_secret = 'pHVnoNN1GDL38RpYYDGNnscxrnATGwTc7nSM8WpBAXjztIXBGI'
access_token = '1196316237774520324-qOWElgJgsKSRWKHj6m5TtDKsb7bsJF'
access_secret = 'AYsG1B9Tq3mKEuXScxThFMmdie9zO3USMATOMS1s6sHuh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
keyword = '겨울왕국2'
result = []
file_mingu = open("result_data_twitter.txt","a")

for i in range(1, 20):
    tweets = api.search(keyword)
    for tweet in tweets:
        file_mingu.write(str(tweet))
        result.append(tweet)    
