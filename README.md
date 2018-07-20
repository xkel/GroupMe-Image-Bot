# GroupMe-Image-Scraper-Bot

This is a bot that I developed in Python to be able to easily save all images ever shared in a group to file system. I wrote this application because it served to be especially ideal for groups where memorable photos are shared and potentially 100s to over 1000s over messages and images have already been shared.

## Getting Started

If you'd like to use this bot for your own group or development simply clone the project on your machine. Navigate to the root project directory in a terminal, and from that point on simply type 'Python3 app.py'.

It is necessary to configure your own environment variables. Specify a '.env' file in the root directory of the project. The project uses GroupMe tokens so you'll need to create your own bot (passive) at first at dev.groupme.com. GroupMe should then give you all the necessary variables.

In the .env file:

bot_id="YOUR BOT ID"
token="YOUR USER TOKEN"
group_ID="THE GROUP ID"

On start the application saves all previously shared images, and then proceeds to listen for any new images that my be shared.

### Deployment

You may consider deploying the bot to a cloud server such as Heroku, keep in mind that I intended for images to write to file system so you may have to configure a solution on the cloud to have images write to a database.

##### Prerequisites

Python 3.6.5

It is essential to have the necessary Python modules installed such as:
Flask
Pip
Requests
and python-dotenv

## Dependency Resolution
Generate your own requirements file by using the command:
pip freeze > 'filename' (typically: 'requirements.txt')

then resolve dependencies with the command:
pip install -r requirements.txt

## Unit Testing
unittest is a standard module which does not need to be installed.

run the command: python3 -m unittest from the terminal.

Developers have the option of installing unittest2 which is a back-port of unittest for Python2.6,
however that is not necessary for this project.
