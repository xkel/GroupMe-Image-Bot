from flask import Flask, request
import bot
import imgur

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        return "I'm a simple GroupMe bot built with Python, I save pictures from a group"
    else:
        response = request.get_json()
        # if the message received is just text with no image
        if(response['attachments'] == []):
            print(response['text'])
        else: # the message is an image so posti t
            if(response['attachments'][0]['type'] == 'image'):
                print(response['attachments'][0]['url'])
        return 'good'    

if __name__ == '__main__':
    app.run()