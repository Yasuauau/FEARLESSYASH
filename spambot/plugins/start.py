from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon import events, Button


data  = [
    Button.url("Sᴜᴘᴘᴏʀᴛ ⚙", url="t.me/tso_chats"),
    Button.url("Uᴘᴅᴀᴛᴇs 🚀", url="t.me/tso_updates"),
    Button.url("Sᴏᴜʀᴄᴇ 📡", url="https://GitHub.com/wastertso")
]


@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Tʜᴇ Sʜɪᴠ Oғғɪᴄɪᴀʟ](t.me/ll_tso_king_ll})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hᴇʏ 🍷 {mention},

Tʜɪs ɪs Tsᴏ Sᴘᴀᴍ Bᴏᴛ ⋟ 😈

Oᴡɴᴇʀ 💸 :- {myOwner}

Sᴜᴅᴏ 🥷 :- {sudo_user}

Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)

