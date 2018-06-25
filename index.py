import requests
import config

def main():
    url = 'https://api.groupme.com/v3/bots/post'
    headers = {'Content-Type': 'application/JSON'}
    params = {'token': config.token, 'text': 'Are my keys safe?', 'bot_id': config.bot_id}
    makeRequest(url, headers, params)


def makeRequest(url, headers, params):
    r = requests.post(url, headers = headers, params = params)
    print(r.text)


main()
