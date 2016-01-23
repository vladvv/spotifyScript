#!/usr/bin/env python
import httplib2 as http
import json
import urllib
import requests
import base64

AUTH_URL = 'https://accounts.spotify.com/authorize/'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
PLAYLIST_URL = 'https://api.spotify.com/v1/users/spotifydiscover/playlists/6rnTWcYUgkqWI0KVw2JKa0/tracks'
CLIENT_ID = '9c77c65339dc4d2a867af5928add5e0b'
CLIENT_SECRET = 'db336d1726804c4bbd47c33aca4e70c7'
CALLBACK_URL = 'http://www.bing.com'

def fetchPlaylist():
	headers = {
		'Authorization': 'Bearer BQD0nooz0YptUKsWSq5W0YINNpweazFk-nAkmjXL8WaGsxS0HxUbz84q3aEO1mMISdYfpjwa9Rq0KhRFwcpUf4En1t8C35zL7fyp-2-B9d5XdbdaSZgDIN_TFv64gEwHIztXrwa_rg'
	}

	response = requests.get(PLAYLIST_URL, headers = headers)

	data = response.json()


	for item in data['items']:
		print item['track']['name'] + ' by ' + item['track']['artists'][0]['name']

def auth():
	params = { 	"client_id":"9c77c65339dc4d2a867af5928add5e0b",
				"response_type":"code",
				"redirect_uri": CALLBACK_URL}

	print AUTH_URL + "?" + urllib.urlencode(params)


def requestTokens():
	data = { 	"grant_type":"authorization_code",
					"code":"AQChqLEPbdiqr11eZYXNwB-7IN0oD2kr9jjeNt1AYYntNGQVSBGjE_4bUf1shYcQcHnLg9fH8OGxmk7-W8KSXgfoPBU_fyI9C6DYHBICLh-i52QAYwJCsGV3eRN7QqA0JBIRviin81h1k9V9-G_2FZejGqAADtKlDeASZ7eevUWhg1vUPHOeFvU",
					"redirect_uri":CALLBACK_URL,
					"client_id":CLIENT_ID,
					"client_secret":CLIENT_SECRET
	}

	authstring = 'Basic ' + CLIENT_ID + ':' + CLIENT_SECRET
	headers = {	'Authorization' : base64.b64encode(authstring) }

	response = requests.post(TOKEN_URL, data = data)
	print response.json()

#auth()
#requestTokens()
fetchPlaylist()





#"AQCCbOl_ZomwA8clifS35sisKClu5JlUQXfhSMOJFNbKE2GFqPAK2Aie6P9P9iqsgYFHSkr6uaEl-Q_brOnisUX0Wyrvvnk-GEXK-4TibNoM6G2WGoDYw0LO_FD2ZAJK-ztFqsN2XYZ5l4zRGfL0PhfYtsUFGQRw8_S1D40d299fPdr5jXKLMBQ"