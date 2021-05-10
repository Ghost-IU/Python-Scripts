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
 
search_string = 'YOUR_SEARCH_STRING'
numberOfTweets = 2 #Can be chaged based on your needs.           

for tweet in limlit_handler(tweepy.Cursor(api.search,search_string).items(numberOfTweets):
  try:
    tweet.favorite()
    print("Tweet added to your favourites list!!") 
  except tweepy.TweepError as err:
    print(e.reason)
  except StopIteration:
    break
