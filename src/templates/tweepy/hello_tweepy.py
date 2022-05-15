#####################################################
################ TWEEPY EXAMPLES ####################
#####################################################
"""
    This file contains multiple examples of TWEEPY Usage.
"""

import tweepy
from dotenv import dotenv_values
import logging

logger = logging.getLogger("tweepy_examples")

######## AUTHENTICATION ########
"""
    Twitter requires all requests to use OAuth for authentication.
    The Authentication documentation goes into more details about authentication:
    https://docs.tweepy.org/en/stable/authentication.html#authentication
"""

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
logger.info("Authentication Completed.")

################################
########### EXAMPLES ###########
################################
"""
    Example 1: downloading your home timeline tweets and print each one of their texts to the console.
"""
logger.info("Running example 1: downloading your home timeline tweets and print each one of their texts to the console.")
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


"""
    Example 2: Using the Tweepy api class to get information about a twitter user
"""
logger.info("Running example 2: Using the Tweepy api class to get information about a twitter user")
user = api.get_user(screen_name="kooshatp")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
