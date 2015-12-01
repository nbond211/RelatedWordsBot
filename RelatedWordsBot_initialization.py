__author__ = 'Nicholas'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import requests
import random
import urllib2
import simplejson
import cStringIO
from PIL import Image


# Links this bot to the Twitter account: RelatedWordsBot
CONSUMER_KEY = 'I9UkSxDNjbvYDtUQnmJGF2SAH'
CONSUMER_SECRET = 'YkEv5PXQtaux1yf8duN1CUYWPaMpyroBQSNXmN24fmHiAQtDMd'
ACCESS_KEY = '4340105542-dBRVFG4Z4MFjsHmZq7gBHO98rH2rHfyxMsjftJp'
ACCESS_SECRET = 'oUEbFlcQBCYnp1fRKbGNefegyLPsEs3DwjVVCqx9RdnGF'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# List of all words in English language
word_site = "http://www.mieliestronk.com/corncob_lowercase.txt"
# Generate a list of words
response = requests.get(word_site)
WORDS = response.content.splitlines()

fetcher = urllib2.build_opener()

# Choose a random word to be the search term
searchTerm = random.choice(WORDS).decode("utf-8")
startIndex = 0
# Search for the word on Google Images
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)
# Download first image from Google Images
imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
file = cStringIO.StringIO(urllib2.urlopen(imageUrl).read())
img = Image.open(file)
# Update Twitter status with downloaded image
api.update_with_media(filename="image.jpg", status=searchTerm.capitalize(), file=file)

