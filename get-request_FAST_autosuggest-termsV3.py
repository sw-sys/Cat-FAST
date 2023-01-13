# Resources https://github.com/sw-sys/Cat-FAST
#
# print(help(response)) for more information
#
#

import requests
import JSON
from bs4 import BeautifulSoup
from pyfiglet import figlet_format

print("Search for a FAST subject heading with")
print(figlet_format("FAST-inSH", font = "bigchief"))

print("Type in the 3-digit MARC field code and press ENTER\n")

# Dictionary for MARC fields and API search facets
MARC_dict_lookup = {
    "600": "suggest00", # personal names
    "610": "suggest10", # corporate names
    "611": "suggestall", # *meetings*
    "630": "suggestall", #uniform titles
    "647": "suggest11", #named event
    #"648": "", #chronological term
    "650": "suggest50", #topical term
    "651": "suggest51", # geographic name
    #"653": "", #index term - uncontrolled
    "654": "suggest50", # *subject added entry - faceted topical terms*
    "655": "suggest55", # index term - genre/form
    #"656": "", #index term - occupation
    #"657": "", #index term - function
    #"658"; "", #index term - curriculum objective
    "662": "suggest51", # Subject added entry - hierachical place name
    "688": "suggestall", # subject added entry - type of entity unspecified
    "69X": "suggestall", #Local subject acces fields
    }

### User input - Variables to define FAST search  ###
m_number = input("MARC subject field: ") 
facet = MARC_dict_lookup[m_number]

print("\nNow type your search term and press ENTER\n")
query = input("Search term: ")

#parameters to be passed to API
payload = {"query": query, "fl": facet, "rows": 10}

### requesting info about search from URL via Requests module ### 
response = requests.get("http://fast.oclc.org/searchfast/fastsuggest?", params=payload)

# printing info gathered from FAST API ###
json_r = (response.json())
for item in json_r:
    JSON.stringify(response)
    print(response)

#print(json_r)

###PARSING response TO GET SUGGESTED FAST TERMS###
#Split response

# suggestions = raw_sugs.split(":")[15]
# print(raw_sugs)

#input("Press ENTER to exit")