import config
import requests
import json
import imgur

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

def getBinaryData(url):
    r_file = requests.get(url)
    content = r_file.content
    imgData = BytesIO(content)
    return imgData

    # with open('test.txt', 'wb') as fd:
    #     #for chunk in r_file.iter_content(chunk_size=128):
    #         fd.write(content)

def push_img(img):

    req = requests.post('http://313fae50.ngrok.io', data = img)
    if(req.status_code == 200):
        print('success')


# Prints all messages posted in a specified group chat (group id)
# Note: Hard-coded group ID in
def get_images():
    base_url = 'https://api.groupme.com/v3'
    url = '/groups/41498316/messages'
    params = {'token': config.token} # before_id, since_id, after_id
    messagesResponse = requests.get(base_url + url, params = params).json()
    msg_count = messagesResponse['response']['count']
    img_list = []
    i = 0
    x = 0
    while i < msg_count:
        if(x < 20):
            #print(messagesResponse['response']['messages'][x]['text'], (i+1))
            if messagesResponse['response']['messages'][x]['attachments']:
                img_url = messagesResponse['response']['messages'][x]['attachments'][0]['url']
                img_list.append(img_url)
            if(x == 19):
                id = messagesResponse['response']['messages'][x]['id'] 
            x += 1
        else:
            params = {'token': config.token, 'before_id': id} # before_id, since_id, after_id
            messagesResponse = requests.get(base_url + url, params = params).json()
            x = 0
        i += 1
    return img_list