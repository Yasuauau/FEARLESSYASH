from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from spambot.help import *
from spambot.helpers.commands import *
from telethon import events


@MafiaBot1.on(events.CallbackQuery(data=b'alive'))
@MafiaBot2.on(events.CallbackQuery(data=b'alive'))
@MafiaBot3.on(events.CallbackQuery(data=b'alive'))
@MafiaBot4.on(events.CallbackQuery(data=b'alive'))
@MafiaBot5.on(events.CallbackQuery(data=b'alive'))
async def alive_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'ping'))
@MafiaBot2.on(events.CallbackQuery(data=b'ping'))
@MafiaBot3.on(events.CallbackQuery(data=b'ping'))
@MafiaBot4.on(events.CallbackQuery(data=b'ping'))
@MafiaBot5.on(events.CallbackQuery(data=b'ping'))
async def ping_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'raid'))
@MafiaBot2.on(events.CallbackQuery(data=b'raid'))
@MafiaBot3.on(events.CallbackQuery(data=b'raid'))
@MafiaBot4.on(events.CallbackQuery(data=b'raid'))
@MafiaBot5.on(events.CallbackQuery(data=b'raid'))
async def raid_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot2.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot3.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot4.on(events.CallbackQuery(data=b'replyraid'))
@MafiaBot5.on(events.CallbackQuery(data=b'replyraid'))
async def replyraid_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'spam'))
@MafiaBot2.on(events.CallbackQuery(data=b'spam'))
@MafiaBot3.on(events.CallbackQuery(data=b'spam'))
@MafiaBot4.on(events.CallbackQuery(data=b'spam'))
@MafiaBot5.on(events.CallbackQuery(data=b'spam'))
async def spam_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot2.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot3.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot4.on(events.CallbackQuery(data=b'pspam'))
@MafiaBot5.on(events.CallbackQuery(data=b'pspam'))
async def pspam_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'extras'))
@MafiaBot2.on(events.CallbackQuery(data=b'extras'))
@MafiaBot3.on(events.CallbackQuery(data=b'extras'))
@MafiaBot4.on(events.CallbackQuery(data=b'extras'))
@MafiaBot5.on(events.CallbackQuery(data=b'extras'))
async def extras_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'heroku'))
@MafiaBot2.on(events.CallbackQuery(data=b'heroku'))
@MafiaBot3.on(events.CallbackQuery(data=b'heroku'))
@MafiaBot4.on(events.CallbackQuery(data=b'heroku'))
@MafiaBot5.on(events.CallbackQuery(data=b'heroku'))
async def heroku(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{HEROKU_CMD}", buttons=BACK)

@MafiaBot1.on(events.CallbackQuery(data=b'back'))
@MafiaBot2.on(events.CallbackQuery(data=b'back'))
@MafiaBot3.on(events.CallbackQuery(data=b'back'))
@MafiaBot4.on(events.CallbackQuery(data=b'back'))
@MafiaBot5.on(events.CallbackQuery(data=b'back'))
async def back_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 
