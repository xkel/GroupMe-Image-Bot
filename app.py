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
        return "I'm a simple GroupMe bot built with Python, I take and save pictures shared in a group chat"
    else: # issue response to the received post request (message)
        response = request.get_json()
        # if the message received is just text with no image
        if(response['attachments'] == []):
            pass
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
                        print('Image: ' + filename + ' saved')               
        return 'good'    

if __name__ == '__main__':
    this_dir = os.getcwd()
    img_file = this_dir + '/imgs'
    bot_inst = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])

    if not os.path.isdir(img_file):
        print('Creating image folder at: ' + img_file)
        os.mkdir(img_file)
        print('Populating image folder at: ' + img_file + ' this may take a moment')
        bot_inst.run()
        print('')
        print('Finished')

    print('Listening for new images')
    app.run()
