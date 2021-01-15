#!/usr/bin/python

import requests
import sys

# gets the requests in res variable
res = requests.get(sys.argv[2])
if res.status_code == 200:
    # Takes the key from the res for iteration of all keys
    for key in res.json()['keys']:
        # appends the key for getting each key value pair
        getKeyValPair = requests.get(sys.argv[2] + "/" + key)
        # prints the available Key Value pairs
        print(getKeyValPair.text)
else:
    print("Something went wrong")