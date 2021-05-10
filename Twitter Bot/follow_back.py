#      Apache License
#      Version 2.0, January 2004
#      http://www.apache.org/licenses/

import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
printf(f"Hey {user.name()}")

def limlit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(500)
 
user_name = 'NAME'   
for follower in limit_handler(tweepy.Cursor(api.followers).items():
  if follower.name == user_name:
    follower.follow()
    print(f'Started following {user_name}!')
    break
