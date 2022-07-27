from flask import Flask, request
from dotenv import load_dotenv
import bot
import os
import unittest

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class TestBotApp(unittest.TestCase):
    def test_postImages(self):
        """Does the bot save images to imgs folder?""" # GIVEN the group chat has at least one image
        testBot = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])
        testBot.run() #THEN the bot should save images from the group to the imgs folder
        self.assertTrue(len(os.listdir('./imgs')) > 0) #AND there should be at least one image in the folder

    def test_postMessage(self):
        """Does the bot post messages to the group?""" #GIVEN the appropriate environment variables are configured
        testBot = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])
        status = testBot.postMessage('Zygium') #WHEN the bot posts a message
        self.assertTrue(status == 202) # a status code of 202 should be returned

    def test_getImages(self):
        """Does the bot retrieve a list of images?""" # GIVEN the group chat has at least one image
        testBot = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])
        imageList = testBot.run() #AND THEN post_images calls the private get_images method which returns an array
        self.assertTrue(len(imageList) > 0) #THEN there should be at least one element in the array
