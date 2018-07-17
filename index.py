
# file is used for testing
if __name__ == "__main__":
    # img_list = bot.get_images() # grabs images from group history in the GroupMe by URL
    # imgur.post_images(img_list) # posts images to the Imgur account with an array 
    # img_IDs = imgur.get_imgIDs()
    # imgur.post_album(img_IDs) 


    # def __get_images(self):
    #     base_url = 'https://api.groupme.com/v3'
    #     url = f'/groups/{self.group_id}/messages'
    #     params = {'token': self.auth_token} # before_id, since_id, after_id
    #     messagesResponse = requests.get(base_url + url, params = params).json()
    #     msg_count = messagesResponse['response']['count']
    #     img_list = []
    #     i = 0
    #     x = 0
    #     while i < msg_count:
    #         if(x < 20):
    #             #print(messagesResponse['response']['messages'][x]['text'], (i+1))
    #             if messagesResponse['response']['messages'][x]['attachments']:
    #                 img_url = messagesResponse['response']['messages'][x]['attachments'][0]['url']
    #                 img_list.append(img_url)
    #             if(x == 19):
    #                 id = messagesResponse['response']['messages'][x]['id'] 
    #             x += 1
    #         else:
    #             params = {'token': self.auth_token, 'before_id': id} # before_id, since_id, after_id
    #             messagesResponse = requests.get(base_url + url, params = params).json()
    #             x = 0
    #         i += 1
    #     return img_list