from flask import Flask, request
from dotenv import load_dotenv
import bot
import os
import imgur
import requests


from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        return "I'm a simple GroupMe bot built with Python, I post pictures shared in a group to imgur"
    else:
        response = request.get_json()
        # if the message received is just text with no image
        if(response['attachments'] == []):
            print(response['text'])
        else: # the message is an image so post it
            if(response['attachments'][0]['type'] == 'image'):
                print(response['attachments'][0]['url'])
                img_url = response['attachments'][0]['url']
                filename = img_url.split('/')[-1]
                r = requests.get(img_url, stream=True)
                if r.status_code == 200:
                    content_type = r.headers['content-type']
                    file_type = content_type.split('/')[-1]
                    print(content_type)  
                    with open('./imgs/' + filename + '.' + file_type, 'wb') as f:
                        for chunk in r:
                            f.write(chunk)                
                
                #imgur.post_img(img_url)
        return 'good'    

if __name__ == '__main__':
    
    bot1 = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])
    #check to see if imgs folder is already populated prior to running
    if not os.listdir('./imgs/'):
        bot1.post_images_FS()
    app.run()