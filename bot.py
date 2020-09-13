from instabot import Bot

bot=Bot()

#enter the username and password in the respective fileds

bot.login(username="enter the username here", password="enter the password here")

#enter the image that has to be posted

bot.upload_photo("enter the image here with img type", caption="enter the caption here with hastags!")
