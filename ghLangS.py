import os
from dotenv import load_dotenv
import requests


load_dotenv()
GH_AT = os.getenv('GH_AUTH_TOKEN')

if not GH_AT:
    print("Github AUTH_TOKEN not found! We can't continue :-/")
    print("Please review your .env file")
    exit(1)


response = requests.get('https://api.github.com/repos/lsst-it/lsst-control/languages', headers={'Authorization': "Bearer {}".format(GH_AT) })

print(response.json())

