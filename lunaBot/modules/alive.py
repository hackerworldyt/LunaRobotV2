import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/448204079c7b3d5d91587.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Hello I Am Hw Music Bot!** \n\n"
  LUNA += "🔴 **I'm Working Properly** \n\n"
  LUNA += "🔴 **My Master : [нαcкεя ωσяℓ∂](https://t.me/iamhackerworld)** \n\n"
  LUNA += f"🔴 **Telethon Version : {tlhver}** \n\n"
  LUNA += f"🔴 **Pyrogram Version : {pyrover}** \n\n"
  LUNA += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/hwmusicbot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/iamhackerworld")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "✅ **bot restarted successfully**\n\n• Admin list has been **updated**"
  BUTTON = [[Button.url("📡 ᴜᴘᴅᴀᴛᴇs", "https://t.me/HwBotSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
