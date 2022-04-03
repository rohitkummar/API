
# Sample Program to learn api 

# Libraries required: requests, json

import requests
import json

# target url
url="https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

# request made to specified url
response=requests.get(url)


# received data converted to jason data structure
data = response.json()

# checking the connection with url
if response !=404:
    for y in data['items']:
        print(y['title'])