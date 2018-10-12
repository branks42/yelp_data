import requests
from requests_oauthlib import OAuth1

consumer_key = 'CONSUMERKEY'
consumer_secret = 'CONSUMERSECRET'
token = 'TOKENKEY'
token_secret = 'TOKENSECRET'

auth = OAuth1(consumer_key, consumer_secret, token, token_secret)

def do_search(term='Food', location='Atlanta'):
	base_url = 'https://api.yelp.com/v2/search'

	params = {
		'term': term,
		'location': location,
	}

	auth = OAuth1(consumer_key, consumer_secret, token, token_secret)
	r = requests.get(url, auth=auth, params=params)
	return r.json()

search_1 = do_search()

for i in search_1['businesses']:
	print(i['name'])
	print(i['phone'])
	print(i['website'])
