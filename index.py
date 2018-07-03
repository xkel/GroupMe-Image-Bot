import bot
import imgur

if __name__ == "__main__":
    img_list = bot.get_images() # grabs images from group history in the GroupMe by URL
    imgur.post_images(img_list) # posts images to the Imgur account with an array 
    img_IDs = imgur.get_imgIDs()
    imgur.post_album(img_IDs) 