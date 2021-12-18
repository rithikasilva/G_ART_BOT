import tweepy
import os


# Tweets image in working folder with the input number provided for tweet
def tweet_image(number):

    api_key = os.environ['API_KEY']
    secret_key = os.environ['SECRET_KEY']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(access_token, access_token_secret)


    # Create API object
    api = tweepy.API(auth)
    api.verify_credentials()


    # Upload image
    media = api.media_upload("./working/image_temp.png")

    # Post tweet with image
    tweet = "Number: " + str(number)
    api.update_status(status=tweet, media_ids=[media.media_id])




