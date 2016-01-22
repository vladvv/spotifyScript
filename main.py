#!/usr/bin/env python
import httplib2 as http
import json

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


headers = {
	'Authorization': 'Bearer BQAyYKHiq7xtU62YC5RHQi4NgGguLj3GNZj3Ii5kn4DpsogduulTCXmap-Q9uJiasded6qvBiaILJ05bEc702vwD5zA9QyN7sljKBVWpCcZfL_8kV9RuXH34kNg8QxP3jtdzEa4J0GobNm8t1hMDJ6eY8cJmqwH_IEdkas25XaQ1m11SSRzhQ4oZF6ywNP7RncuaSWag82UHmgoGaPc-R-vgYsTQXUuKL6lP16t4mJwC-mOEdup4fQ'
}

uri = 'https://api.spotify.com/v1/users/spotifydiscover/playlists/6rnTWcYUgkqWI0KVw2JKa0/tracks'

target = urlparse(uri)
method = 'GET'

h = http.Http()

response, content = h.request(
	target.geturl(),
	method,
	'',
	headers)

print content
