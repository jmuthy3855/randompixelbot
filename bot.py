import tweepy
import time
from numpy import random
import randompixel
from settings import *

key = ACCESS_TOKEN 
secret = SECRET_ACCESS_TOKEN 

consumer_key = API_KEY 
consumer_secret = SECRET_API_KEY

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #twitter authentification system using tokens/keys
auth.set_access_token(key, secret)

#main api object used for bot features
api = tweepy.API(auth)

# tweet out a random cell auto
def tweet():
    randompixel.genRandomCellAuto() 

    img_filename = PHOTO_LOCATION 
    img = api.media_upload(img_filename) #creates twitter object for image
    media_id = [img.media_id] #id list associated with media(image(s))
    api.update_status(status=(''), media_ids=media_id)


def main():
    tweet()
    print("tweeted random cell auto")


if __name__ == '__main__':
    main()
