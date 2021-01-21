import tweepy
import time
from numpy import random
import randompixel
from settings import *

# import randompixel.py here

key = ACCESS_TOKEN #access token
secret = SECRET_ACCESS_TOKEN #access token secret

consumer_key = API_KEY #api key
consumer_secret = SECRET_API_KEY #api key secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #twitter authentification system using tokens/keys
auth.set_access_token(key, secret)

#main api object used for bot features
api = tweepy.API(auth)

def tweet():
    randompixel.genRandomCellAuto() #generate random pixel image

    img_filename = PHOTO_LOCATION #"C:\\Users\\jeymu\\Desktop\\TwitterBot\\resultimg.png"
    img = api.media_upload(img_filename) #creates twitter object for image
    media_id = [img.media_id] #id list associated with media(image(s))
    api.update_status(status=(''), media_ids=media_id)



def main():
    tweet()
    print("tweeted random cell auto")


if __name__ == '__main__':
    main()


'''
future updates:
tweet a random pic to someone who tags the bot
logging so if a crash occurs, i can know what potentially went wrong

'''