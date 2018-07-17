# GroupMe-Image-Scraper-Bot
A bot developed in Python to scrape images shared in a group and save them.

Back-end:
For now I'm choosing to simply use Imgur's API to be able to take an image and use a post request to save it in an album.

bot.py class
- instantiated with environment (.env) variables. provide a bot ID, user auth token and group ID in the instantiation
- example: my_bot = bot.Bot(os.environ['bot_id'], os.environ['token'], os.environ['group_ID'])