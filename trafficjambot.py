import tweepy
import emoji
from os import environ
import time
from emojis import cars,weather,terrain
import random

#Twitter API Keys
CONSUMER_KEY =  environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

api = tweepy.api
size_col=29
size_traffic=9

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth.secure = True
api = tweepy.API(auth)

def traffic():
    weigth = {}
    sumWeg = 0
    
    for k,v in cars.items():
        r = random.randint(0,50)
        sumWeg+=r*k
        weigth[v]=r*k

    #Perfect of whites spaces
    for _ in range(random.randint(0,20)):
        r = random.randint(0,50)
        sumWeg+=r*k
        weigth[' ']=r*k


    message = ''
    for _ in range(size_traffic):
        w = random.randint(0,sumWeg)
        for item,val in weigth.items():
            w -= val           
            if w <=0:
              message+=item
              break
    return message

def background():
    back=''
    return back

def message():
    w = {'moon' : weather[0:9],
       'sun' : weather[10:15],
       'cloud' : weather[16:20],
       'snow' : ':snowflake:',
       'rainbow' : ':rainbow:'}

    # o sol o luna o solo nubes o nada...
    sky = w[random.choice(['moon','sun','cloud'])];
    
    new='' + ('' * random.randint(0,3))
    new+= random.choice(sky)
    
    message= ''.join(new) + '\n'
    message+='_' * 30 + '\n'

    message+=traffic() + '\n'
    message+=traffic() + '\n'
    message+='_' * 30 + '\n'
    

    return message

def tweet(message):
    message = message
    encoded=emoji.emojize(message, use_aliases=True).encode('utf-8')
    print(encoded)
    #print(message.encode('utf-8'))
    
    api.update_status(status=emoji.emojize(message).encode('utf-8'))

if __name__ == '__main__':  
    tweet(message())    
    print("Done")

