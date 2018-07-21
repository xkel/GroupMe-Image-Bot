# WIP

import requests
import json

config = {
    base_url: 'https://photoslibrary.googleapis.com/v1/uploads'
    clientID: 'ID HERE'
    clientSecret: 'SECRET HERE'

}

def upload_image(url, headers=headers):
    headers = {
        'Content-Type': 'application/octet-stream'
        'Authorization': 'Bearer ' + OAUTH2_TOKEN
    }
    requests.post(url)

def upload_album():
    pass