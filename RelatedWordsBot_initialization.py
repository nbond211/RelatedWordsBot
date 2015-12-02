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

# Download image using Bing Search
bing_url = 'https://api.datamarket.azure.com/Bing/Search/Image'
bing_api_key = 'b+otGGjd4HkdQTANFMjLpgaOEmTGDtR38z5JBlCwGPw'
bing_auth = requests.auth.HTTPBasicAuth(bing_api_key, bing_api_key)
bing_page_count = 1
bing_headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'}

def getFirstImg(subject):

    payload = {
        'Query':('\'' + subject + '\''),
        '$format': 'json',
        '$top':bing_page_count,
    }

    search_response = requests.get(bing_url, auth=bing_auth, params=payload, headers=bing_headers)

    try:
        search_response_json = search_response.json()
        return search_response_json['d']['results'][0]['MediaUrl']
    except:
        print('Search error: ' + search_response.text)
        return None


imageUrl = getFirstImg(searchTerm)
file = cStringIO.StringIO(urllib2.urlopen(imageUrl).read())
img = Image.open(file)
# Update Twitter status with downloaded image
api.update_with_media(filename="image.jpg", status=searchTerm.capitalize(), file=file)

