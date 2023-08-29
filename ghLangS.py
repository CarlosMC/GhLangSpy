import os
import requests
from dotenv import load_dotenv

###
# load GH_AUTH_TOKEN form .env file
###
def getGithubAuthToken():
    load_dotenv()
    GH_AT = os.getenv('GH_AUTH_TOKEN')

    if not GH_AT:
        print("Github AUTH_TOKEN not found! We can't continue :-/")
        print("Please review your .env file")
        exit(1)

    return GH_AT

###
# Get languages list from repo, return json object
###
def getLangList():
    gh_at=getGithubAuthToken()

    apiRepoURL = 'https://api.github.com/repos/lsst-it/lsst-control/languages'

    myHeader = {'Accept': 'application/vnd.github+json',
                'Authorization': f"Bearer {gh_at}",
                'X-GitHub-Api-Version': '2022-11-28'}

    try:
        response = requests.get(apiRepoURL, headers=myHeader)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response.json()

###
# Display results in megabytes per lang and the sume of bytes in gigabytes
###
def displayResults(jsonLangs):
    sumBytes = 0

    for langName in jsonLangs:
            nBytes = jsonLangs[langName]
            sumBytes += nBytes
            nMegabytes = nBytes / (1<<20)
            print(f"{langName} with {nMegabytes} megabytes of code")

    nGigabytes = sumBytes / (1<<30)
    print(f"\nTotal gigabytes of code : {nGigabytes}")

###
# Starting from here!
###
def main():

    lanList = getLangList()
    displayResults(lanList)


if __name__ == "__main__":
    main()
