from RawDataMiners import RawDataMiner
from dotenv import load_dotenv
import os
import logging
import twitter

class TweetsMiner(RawDataMiner):
    """

    """
    def __init__(self):
        load_dotenv()
        self.consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
        self.consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
        self.oauth_token = os.environ.get("TWITTER_OAUTH_TOKEN")
        self.oauth_token_secret = os.environ.get("TWITTER_OAUTH_TOKEN_SECRET")
        self.api_object = None

    def getAPIObject(self):
        if self.api_object == None:
            try:
                auth  = twitter.oauth.OAuth(self.oauth_token, self.oauth_token_secret, self.consumer_key, self.consumer_secret)
                self.api_object = twitter.Twitter(auth=auth)
            except:
                logging.error("Cannot connect to Twitter API")

        return self.api_object

if __name__ == '__main__':
    tweets_miner = TweetsMiner()
    print(tweets_miner.getAPIObject())