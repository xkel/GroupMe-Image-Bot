import config
import requests
import json


# series of http requests for imgur

# imgur only allows you to post images directly to an album if they are already 'owned' by you
# you must post an image directly to your account

def imgur_post(img):

    # if img is a url
    headers = {
        'Authorization': 'Bearer ' + config.imgur_token
    }
    params =  {
        'image': img
    }
    r = requests.post('https://api.imgur.com/3/image', headers = headers, params = params)
    print(r.text)
    print(r.status_code)