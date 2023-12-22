
import asyncio
import os

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified

#▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▒▒▒▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▇▇▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▇▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▆▆▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▜▒▒▇▇▒▒▆▆▆▆▆▆▆▆▆
#▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▙▇▇▇▇▇▇▉▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▇
#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒𝐊𝐈𝐌𝐌𝐘 𝐊𝐈𝐍𝐆 𝐕𝐄𝐆𝐀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒






@app.on_message(command(["الاوامر", "اوامر"]))
async def zdatsr(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/d82d7878acd80198a96a2.jpg",
        caption=f"""**مرحبآ بك عزيزي »\n│ \n└ʙʏ: {message.from_user.mention}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★᚜ اوامر اساسيه ᚛★", callback_data="vegax"),
                ],[
                    InlineKeyboardButton(
                        "★᚜ اوامر الادمن ᚛★", callback_data="honakks"),
                    InlineKeyboardButton(
                        "★᚜ اوامر القناه ᚛★", callback_data="alskksks"),
                ],[
                    InlineKeyboardButton(
                       "★𝙎𝙊𝙐𝙍𝘾𝞝𖢻𝘼𝙑𝘼𝙏𝘼𝙍★", url=f"https://t.me/source_av"),                        
                ],
            ]
        ),
    )



