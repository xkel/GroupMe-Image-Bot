import requests
import json
import imgur

class Bot:

    def __init__(self, botToken, auth, group):
        self.bot_token = botToken
        self.auth_token = auth
        self.group_id = group

    def post_data():
        base_url = 'http://0bb05726.ngrok.io'
        payload = json.dumps({'user': 'pass'})
        
        r = requests.post(base_url, data=payload)
        print(r.status_code)

    def postMessage(self, text): 
        url = '/bots/post'
        params = {'bot_id': self.bot_token, 'text': text}
        self.makePostRequest(url, params)

    def __getBinaryData(url):
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

    # Returns an array of all images shared in a group

    def get_images(self):
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

    def post_all_images(self):
            img_list = self.get_images()
            imgur.post_images(img_list) # posts images to the Imgur account with an array 

    def imageExists(url): # should only be run to check if an image has been shared already
        pass
        
