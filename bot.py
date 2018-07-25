import requests
import json
import imgur

class Bot:

    def __init__(self, botToken, auth, group):
        self.bot_token = botToken
        self.auth_token = auth
        self.group_id = group

    def __makePostRequest(self, url, params):
        base_url = 'https://api.groupme.com/v3'
        r = requests.post(base_url + url, params = params)

        print(r.status_code)
        print(r.text)
        return r.status_code

    def __post_data():
        base_url = 'http://0bb05726.ngrok.io'
        payload = json.dumps({'user': 'pass'})

        r = requests.post(base_url, data=payload)
        print(r.status_code)

    def __getBinaryData(url):
        r_file = requests.get(url)
        content = r_file.content
        return content

        # with open('test.txt', 'wb') as fd:
        #     #for chunk in r_file.iter_content(chunk_size=128):
        #         fd.write(content)

    def __push_img(img):
        req = requests.post('http://0bb05726.ngrok.io', data = img)
        if(req.status_code == 200):
            print('success')

    def postMessage(self, text):
        url = '/bots/post'
        params = {'bot_id': self.bot_token, 'text': text}
        return self.__makePostRequest(url, params)

    # Returns an array of all images shared in a group

    def __get_images(self):
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
                if(messagesResponse['response']['messages'][x]['attachments'] == []):
                    pass
                else:
                    if(messagesResponse['response']['messages'][x]['attachments'][0]['type'] == 'image'): # message should be an image at this point
                        img_url = messagesResponse['response']['messages'][x]['attachments'][0]['url']
                        img_list.append(img_url)
                        print('Image ' + str(i) + '/' + str(msg_count) + ' collected', end='\r')
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

    def __post_images_FS(self):
        img_list = self.__get_images()

        for img_url in img_list:
            filename = img_url.split('/')[-1]
            r = requests.get(img_url, stream=True)
            if r.status_code == 200:
                content_type = r.headers['content-type']
                file_type = content_type.split('/')[-1]
                with open('./imgs/' + filename + '.' + file_type, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
                    print('Image: ' + filename + ' saved', end='\r')
        return img_list


    def imageExists(url): # should only be run to check if an image has been shared already
        pass

    def run(self):
        img_list = self.__post_images_FS()
        return img_list
