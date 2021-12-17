import tweepy
import os
from dotenv import load_dotenv


def tweet_image(number):

    # THIS BLOCK CHANGE FOR LOCAL RUNNING
    load_dotenv()
    api_key = str(os.getenv('API_KEY'))
    secret_key = str(os.getenv('SECRET_KEY'))
    access_token = str(os.getenv('ACCESS_TOKEN'))
    access_token_secret = str(os.getenv('ACCESS_TOKEN_SECRET'))
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



# Create a tweet
#recipient_id = sensitive.my_id  # ID of the user
#api.send_direct_message(recipient_id, "Test Message")

#messages = api.get_direct_messages(count=2)
#for message in reversed(messages):
  # who is sending?
  #sender_id = message.message_create["sender_id"]
  #print(sender_id)
  # what is she saying?
  #text = message.message_create["message_data"]["text"]
  #print(text)

#Remeber to wait because the message takes a couple minutes to appear



