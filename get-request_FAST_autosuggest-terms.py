# OCLC FAST API docs https://www.oclc.org/developer/api/oclc-apis/fast-api/linked-data.en.html

# print(help(response)) for more information
# content - would be good for images
# text - content of page in unicode

### FACETS ###

# All Facets -	suggestall
# Personal Names -	suggest00
# Corporate Names -	suggest10
# Events -	suggest11
# Titles -	suggest30
# Topicals -	suggest50
# Geographics -	suggest51
# Forms -	suggest55
# LC Heading -	refphrase

import requests
from bs4 import BeautifulSoup

### User input - Variables to define FAST search  ###

query = input("Enter your search term: ") # poetry
facet = input("Limit results by Subject Access Field: ") # suggest50

### concatination of URL for API ###
url = "http://fast.oclc.org/searchfast/fastsuggest?query=%s" %query + "&fl=%s" %facet

### requesting info about search from URL via Requests module ###
response = requests.get(url)

### printing info gathered from FAST API ###
print(response.text)