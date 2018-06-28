import config
import requests
import json

from io import BytesIO
from PIL import Image

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

def post_data():
    base_url = 'http://c7dadf45.ngrok.io'
    payload = json.dumps({'user': 'pass'})
    
    r = requests.post(base_url, data=payload)
    print(r.status_code)

def groupMessage(text):
    url = '/bots/post'
    params = {'bot_id': config.bot_id, 'text': text}
    makePostRequest(url, params)

def getFile(url):
    r_file = requests.get(url)
    content = r_file.content

    img = Image.open(BytesIO(content))

    #if succesful display image
    img.show()

    with open('test.txt', 'wb') as fd:
        #for chunk in r_file.iter_content(chunk_size=128):
            fd.write(content)
    
    


    #with open(path, 'wb') as f:)
    #    for chunk in r_file.iter_content():
    #        f.write(chunk)
    #local_file = open(path, 'rb')


# Prints all messages posted in a specified group chat (group id)
# Note: Hard-coded group ID in
def printAllMessages():
    base_url = 'https://api.groupme.com/v3'
    url = '/groups/41498316/messages'
    params = {'token': config.token} # before_id, since_id, after_id
    messagesResponse = requests.get(base_url + url, params = params).json()
    msg_count = messagesResponse['response']['count']
    
    i = 0
    x = 0

    while i < msg_count:
        if(x < 20):
            #print(messagesResponse['response']['messages'][x]['text'], (i+1))
            if messagesResponse['response']['messages'][x]['attachments']:
                img_url = messagesResponse['response']['messages'][x]['attachments'][0]['url']
                getFile(img_url)
                break
            if(x == 19):
                id = messagesResponse['response']['messages'][x]['id'] 
            x += 1
        else:
            params = {'token': config.token, 'before_id': id} # before_id, since_id, after_id
            messagesResponse = requests.get(base_url + url, params = params).json()
            x = 0
        i += 1