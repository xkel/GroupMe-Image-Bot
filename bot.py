#import config
import requests
import json
import imgur

class Bot:

    def __init__(self, botToken, auth, group):
        self.bot_token = botToken
        self.auth_token = auth
        self.group_id = group

    def makePostRequest(self, url, params):
        base_url = 'https://api.groupme.com/v3'
        r = requests.post(base_url + url, params = params)
        
        print(r.status_code)
        print(r.text)
        # if headers is None:
        #     r = requests.post(base_url + url, params = params)
        # elif params is None:
        #     r = requests.post(base_url + url, headers = headers)
        # else:
        #     r = requests.post(base_url + url, headers = headers, params = params)
 
        # print(r.status_code)
        # print(r.text)

    def makeGetRequest(self, url, params, json):
        base_url = 'https://api.groupme.com/v3'
        if json:
            r = requests.get(base_url + url, params = params).json()
        return r
 
        print(r)
        
    # Group ID: 41498316
    def post_data():
        base_url = 'http://0bb05726.ngrok.io'
        payload = json.dumps({'user': 'pass'})
        
        r = requests.post(base_url, data=payload)
        print(r.status_code)

    def postMessage(self, text):
        url = '/bots/post'
        params = {'bot_id': self.bot_token, 'text': text}
        self.makePostRequest(url, params)

    def getBinaryData(url):
        r_file = requests.get(url)
        content = r_file.content
        return content

        # with open('test.txt', 'wb') as fd:
        #     #for chunk in r_file.iter_content(chunk_size=128):
        #         fd.write(content)

    def push_img(img):
        req = requests.post('http://0bb05726.ngrok.io', data = img)
        if(req.status_code == 200):
            print('success')


    # Prints all messages posted in a specified group chat (group id)
    # Note: Hard-coded group ID in
    # should be run upon joining for the first time
    def get_images():
        base_url = 'https://api.groupme.com/v3'
        url = f'/groups/{self.group_id}/messages'
        params = {'token': self.auth_token} # before_id, since_id, after_id
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
                params = {'token': self.auth_token, 'before_id': id} # before_id, since_id, after_id
                messagesResponse = requests.get(base_url + url, params = params).json()
                x = 0
            i += 1
        return img_list