### Here, It's a twitter bot that will automate some functions for you!!

#### The following functions:
* Follow back one or more users.
* Favourite your tweets based on a string passed

#### First things to do:
- Go to [twitter](twitter.com) and go to the API's section.
- Create an app and get your API's and all the necessary tokens.
- Install the [tweepy](https://www.tweepy.org/) library locally on your machine by executing the command:
 ``` pip install tweepy ```
- After creating the app in twitter, get it's __consumer_key__, __consumer_secret__, __access_token__, __access_token_secret__ and replace them respectively in the script.

##### _Follow Back_
- Replace __NAME__ by the username of the user in twitter whom you want to follow back.
- That's it now run ```python3 follow_back.py```
- _If you want to follow multiple users at a time, pass a list to this [loop](https://github.com/Ghost-IU/Python-Scripts/blob/9379d69ac52fb33b1f59ebd564fa6b6b3137daa6/Twitter%20Bot/follow_back.py#L24). 

##### _Favourite a tweet_
- Replace __YOUR_SEARCH_STRING__ by the word which you want to favourite your tweets on.
- You can also vary the __numberOfTweets__ based on how much tweets you want to favourite based on the string you passed.
- Now run the script by using ```python3 favourite_it.py``` 
- Voila! Now head back to twitter and see if it's in your favourites list. 
          
