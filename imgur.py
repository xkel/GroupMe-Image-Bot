import config
import requests
import json


# series of http requests for imgur

# imgur only allows you to post images directly to an album if they are already 'owned' by you
# you must post an image directly to your account

def post_img(img):

    # if img is a url
    headers = {
        'Authorization': 'Bearer ' + config.imgur_token
    }
    params =  {
        'image': img
    }
    r = requests.post('https://api.imgur.com/3/image', headers = headers, params = params)
    print(r.status_code)

def post_images(img_list):
    for item in img_list:
        try:
            post_img(item)
        except requests.exceptions.RequestsException as e:
            print(e)
            sys.exit(1) 


# iterates through the account images and grabs ids
def get_imgIDs():
    
    img_IDs = []
    # get request

    headers = {
        'Authorization': 'Bearer ' + config.imgur_token
    }

    r = requests.get('https://api.imgur.com/3/account/me/images', headers = headers).json()
    data = r['data']
    for item in data:
        img_IDs.append(item['id'])
    return img_IDs

def post_album(img_list):
    headers = {
        'Authorization': 'Bearer ' + config.imgur_token
    }
    params =  {
        'ids[]': img_list
    }
    albumHash = 'k8I6ZgQ'
    url = f'https://api.imgur.com/3/album/{albumHash}/add'
    r = requests.post(url, headers=headers, params=params)
    print(r.text)
    



