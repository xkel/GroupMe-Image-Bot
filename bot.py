import config
import requests

# Group ID: 41498316
def makePostRequest(url, headers = None, params = None):
    base_url = 'https://api.groupme.com/v3'

    if headers is None:
        r = requests.post(base_url + url, params = params)
    elif params is None:
        r = requests.post(base_url + url, headers = headers)
    else:
        r = requests.post(base_url + url, headers = headers, params = params)

    print(r.status_code)
    print(r.text)

def makeGetRequest(url, params, json):
    base_url = 'https://api.groupme.com/v3'
    if json:
        r = requests.get(base_url + url, params = params).json()
        return r

    print(r)

    
# Prints the HTTP response from getting messages in a specified group
# Note: Hard-coded group ID in
def getMessages():
    base_url = 'https://api.groupme.com/v3'
    url = '/groups/41498316/messages'
    #headers = {'Content-Type': 'application/JSON'}
    params = {'token': config.token} # before_id, since_id, after_id
    messagesResponse = requests.get(base_url + url, params = params).json()

    msg_count = messagesResponse['response']['count']
    
    i = 0
    x = 0
    while i < msg_count:
        if(x < 20):
            print(messagesResponse['response']['messages'][x]['text'])
            if(x == 19):
               id = messagesResponse['response']['messages'][x]['id'] 
            x += 1
        else:
            params = {'token': config.token, 'before_id': id} # before_id, since_id, after_id
            messagesResponse = requests.get(base_url + url, params = params).json()
            x = 0
        i += 1
            



    #firstMessage = messagesResponse['response']['messages'][0]['id']
    #print(messagesResponse['response']['messages'][0])
   # print(firstMessage)
