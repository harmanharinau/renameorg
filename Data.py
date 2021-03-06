from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to rename documents and files with certain other features. Use `/help` to learn how !

By @CyniteBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ð  Êá´á´á´ÊÉ´ Êá´á´á´ ð ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("â¨ sá´á´á´á´Êá´ â¨", url="https://t.me/CyniteOfficial")],
        [
            InlineKeyboardButton("Êá´Êá´â", callback_data="help"),
            InlineKeyboardButton("ðª á´Êá´á´á´ ðª", callback_data="about")
        ],
        [InlineKeyboardButton("ð¤á´á´á´á´á´á´sð¤", url="https://t.me/StarkBots")],]

    # Help Message
    HELP = """
Just send a document / video to start renaming. Then when asked, give the new name for the file. The bot will download the file and upload with new name.

1) To have a custom thumbnail on your file, add an 'jpg' image as thumbnail using /thumbnail command.
2) By default, videos are uploaded as videos. To prompt the bot to upload video as document, use /settings to change settings.

â¨ **Available Commands** â¨

/thumbnail - Change thumbnail settings
/settings - Change default settings
/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram rename bot by @CyniteBotsBots

Source Code : [á´ÊÉªá´á´ Êá´Êá´](https://t.me/CyniteOfficial)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @CyniteOfficial
    """
