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
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ sᴜᴘᴘᴏʀᴛ ✨", url="https://t.me/CyniteOfficial")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("🤖ᴜᴘᴅᴀᴛᴇs🤖", url="https://t.me/StarkBots")],]

    # Help Message
    HELP = """
Just send a document / video to start renaming. Then when asked, give the new name for the file. The bot will download the file and upload with new name.

1) To have a custom thumbnail on your file, add an 'jpg' image as thumbnail using /thumbnail command.
2) By default, videos are uploaded as videos. To prompt the bot to upload video as document, use /settings to change settings.

✨ **Available Commands** ✨

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

Source Code : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/CyniteOfficial)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @CyniteOfficial
    """
