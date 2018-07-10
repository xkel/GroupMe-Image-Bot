from flask import Flask, request
from dotenv import load_dotenv
import bot
import os
import imgur

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
                imgur.post_img(img_url)
        return 'good'    

if __name__ == '__main__':
    os.environ['bot_id']
    bot1 = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])
