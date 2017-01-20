

import config
import tweepy

class TwitterAPI(object):

    def __init__(self):
        CONSUMER_KEY = config.CONSUMER_KEY 
        CONSUMER_SECRET = config.CONSUMER_SECRET
        ACCESS_KEY = config.ACCESS_KEY
        ACCESS_SECRET = config.ACCESS_SECRET
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def post_image(self, img_path):
        self.api.update_with_media(img_path, status="#mosaic")
