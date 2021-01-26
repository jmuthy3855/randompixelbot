import tweepy
import time
from numpy import random
import randompixel
from settings import *

# authenticates using keys and returns tweepy API object to be used for bot features
def authenticate():
    key = ACCESS_TOKEN 
    secret = SECRET_ACCESS_TOKEN 

    consumer_key = API_KEY 
    consumer_secret = SECRET_API_KEY

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #twitter authentification system using tokens/keys
    auth.set_access_token(key, secret)

    return tweepy.API(auth)
    

# tweet out a random cell auto
def tweet(tweepy_api):
    img_filename = PHOTO_LOCATION 

    randompixel.gen_random_cellauto(img_filename)

    img = tweepy_api.media_upload(img_filename) #creates twitter object for image
    media_id = [img.media_id] #id list associated with media(image(s))
    tweepy_api.update_status(status=(''), media_ids=media_id)
    print("tweeted random cell auto")
