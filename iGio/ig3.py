import urllib.parse as urlparse
from urllib.parse import parse_qs
url = 'https://www.instagram.com/anabnormalguy/'
parsed = urlparse.urlparse(url)
print(parse_qs(parsed.query)['user_id'])