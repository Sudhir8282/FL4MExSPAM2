from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "SpamX"
pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/5ae11cd68886afe7145d2.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐂ᴅ𝑋sᴘᴀᴍ - ʙʏ ᴛᴇᴀᴍ 𝐂𝐘𝐁𝐄𝐑𝐃𝐑𝐀𝐆𝐎𝐍𝐒"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **𝐌ʏ 𝐁ᴏss😎:** {owner_mention}
➠ **🤖𝐏ʏᴛʜᴏɴ 𝐕ᴇʀsɪᴏɴ🤖:** `{platform.python_version()}`
➠ **🤖𝐂ᴅ𝑋sᴘᴀᴍ 𝐕ᴇʀsɪᴏɴ🤖:** `{__version__}`
➠ **🤖𝐏ʏʀᴏɢʀᴀᴍ 𝐕ᴇʀsɪᴏɴ🤖:** `{pyro_vr}`
➠ **ᴘʏ🤖𝐂𝐘𝐁𝐄𝐑𝐃𝐑𝐀𝐆𝐎𝐍 𝐕ᴇʀsɪᴏɴ🤖:** `{pip_vr}`
➠ **👉𝐂ʜᴀɴɴᴇʟ👈:** @CD_CYBERDRAGONS
━───────╮•╭───────━
➠ **⚡⚡𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗖𝗛𝗔𝗧⚡⚡:** [•ᴄᴅ sᴜᴘᴘᴏʀᴛ•](https://t.me/CD_CHATS)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
