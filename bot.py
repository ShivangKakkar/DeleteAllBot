from pyrogram import idle
from pystark import Stark, plugins
from userbot import userbot


if __name__ == "__main__":
    bot = Stark()
    userbot.start()
    bot.start()
    bot.load_modules('plugins')
    bot.load_modules(plugins.__path__[0])
    directory = plugins.__path__[0]
    Stark.log(f"@{bot.get_me()['username']} is now running...")
    idle()
    bot.stop()
    userbot.stop()
    Stark.log("Bot has stopped working")
