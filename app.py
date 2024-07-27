import tweepy

def create_api():
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def tweet(api, message):
    api.update_status(message)
    print("Tweeted:", message)

api = create_api()
message = input("Enter the tweet: ")
tweet(api, message)
