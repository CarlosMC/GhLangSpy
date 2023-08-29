#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
GH_AT = os.getenv('GH_AUTH_TOKEN')

if not GH_AT:
    print("Github AUTH_TOKEN not found! We can't continue :-/")
    print("Please review your .env file")
    exit(1)


myHeader={'Accept': 'application/vnd.github+json',
            'Authorization': "Bearer {}".format(GH_AT), 
            'X-GitHub-Api-Version': '2022-11-28'}

apiRepoURL='https://api.github.com/repos/lsst-it/lsst-control/languages'

response = requests.get(apiRepoURL, headers=myHeader)

jsonObj=response.json()
sumBytes=0

for langName in jsonObj:
        nBytes = jsonObj[langName]
        sumBytes+=nBytes
        nMegabytes = nBytes / (1<<20)
        print(f"{langName} with {nMegabytes} megabytes of code")

print(f"Total gigabytes of code : {sumBytes/(1<<30)}")

