from flask import Flask, request
import bot
import config
import imgur

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
        else: # the message is an image so posti t
            if(response['attachments'][0]['type'] == 'image'):
                print(response['attachments'][0]['url'])
                img_url = response['attachments'][0]['url']
                imgur.post_img(img_url)
        return 'good'    

if __name__ == '__main__':
    
    bot1 = bot.Bot(config.bot_id, config.token, config.group_ID)
    bot1.post_all_images()
    app.run()