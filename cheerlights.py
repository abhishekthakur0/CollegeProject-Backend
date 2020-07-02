from twython import TwythonStreamer
from sense_emu import SenseHat
from colorzero import Color
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

sense = SenseHat()

hashtag = '#cheerlights'

class CheerlightsStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            tweet = data['text'].replace(hashtag, '')
            print(tweet)

stream = CheerlightsStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track=hashtag)