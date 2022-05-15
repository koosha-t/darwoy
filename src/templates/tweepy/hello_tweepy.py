"""
This example will download your home timeline tweets and print each one of their texts to the console.
Twitter requires all requests to use OAuth for authentication.
The Authentication documentation goes into more details about authentication:
https://docs.tweepy.org/en/stable/authentication.html#authentication
"""

import tweepy
from dotenv import dotenv_values
import logging

logger = logging.getLogger("tweepy_example")

logger.info("reading Twitter credentials from the local .env file in the same folder.")
config = dotenv_values(".env")

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)