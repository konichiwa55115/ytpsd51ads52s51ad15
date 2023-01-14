from bot.util.progress_pyro import get_progress
import time
import asyncio
from bot import LOGGER , TgFileDownloadlist


from pyrogram import Client, filters,StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from plugins.download import ytdl_dowload



@Client.on_message(filters.media)
async def Document_Downloader(client, message):

    await extrastuffs(client,message)
    user_id = str(message.from_user.id)

    try:
        if TgFileDownloadlist[user_id]:
            await message.reply_text(
                "`Multiple Telegram File Download is Not allowed at a same time !!"
                "\nPlease Wait For Complete Your Download `")
            return
    except :
        pass
        
    sentm = await message.reply_text("Hold on !! Preparing For Download...")
    s_time = time.time()
    try:
        TgFileDownloadlist[user_id]={}
        if TgFileDownloadlist[user_id] = True:
            await ytdl_dowload
        else:
            if TgFileDownloadlist[user_id] == False:
                await sentm.edit(f"`Download Cancelled`")
            else:
                await sentm.edit(f"`Download Stopped Due To Some Unknow reason`")
        
    except FloodWait as fw:
        LOGGER.error(fw)
        await message.reply_text(f"FloodWait Sleeping For {fw.x}")

        await asyncio.sleep(fw.x)




        
    finally:
        TgFileDownloadlist[user_id] = False


            

