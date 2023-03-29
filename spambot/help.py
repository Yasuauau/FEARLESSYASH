from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Aʟɪᴠᴇ", b'alive'),
    Button.inline("Pɪɴɢ", b'ping')
], [
    Button.inline("Rᴀɪᴅ", b'raid'),
    Button.inline("Rᴇᴘʟʏ Rᴀɪᴅ", b'replyraid')
], [
    Button.inline("Sᴘᴀᴍ", b'spam'),
    Button.inline("Psᴘᴀᴍ", b'pspam')
], [
    Button.inline("Exᴛʀᴀs", b'extras'),
    Button.inline("Hᴇʀᴏᴋᴜ", b'heroku')
], [
    Button.url("Sᴜᴘᴘᴏʀᴛ ⚙", "t.me/tso_chats"),
    Button.url("Uᴘᴅᴀᴛᴇs 🚀", "t.me/tso_updates")
]

BACK = [
    Button.inline("Back", b'back')
]

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        

