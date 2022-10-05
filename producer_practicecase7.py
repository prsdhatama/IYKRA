import os
os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'

from confluent_kafka import Producer
import tweepy
import time
import json
import time
import logging

api_key ="gcLsaOuuGqm5tKbmIKTcqqBij"
api_secret ="H0zPjJApifM7WQPJrGhKjVQ6criHuE93CYXfBYoUwC01DcWiJEj"
bearer_token =r"AAAAAAAAAAAAAAAAAAAAADpMhwEAAAAAh5GuHI3DmWicyuv6CFVvipXwxLU%3DLulpAMoqgEaz9TpmSgNjjWDY2ec1jVFwTGadR1LyIU3sSLZ0cR"
access_token ="810071851-xXLGzRPzIMpkuoDJI4bCx5xk86LC189wQuMWp8n5"
access_token_secret="afX4DPhJ0CltqKK5hRK8pFiEiCY0ky3PsSRIM5ornYbqM"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

search_terms =["python", "programming", "coding"]

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

################################################
# Specify the producer configuration
p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')
#################################################

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('Connected')

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            # print(tweet.text)
            p.poll(1)
            p.produce('twitter-streaming', tweet.text, callback=receipt)
            p.flush()
            time.sleep(0.2)


############################################
# creating instance
stream = MyStream(bearer_token= bearer_token)
#############################################  

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])


