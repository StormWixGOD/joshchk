#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 18812930, #get it from https://my.telegram.org/auth
    api_hash="fa886be42e33f40f5751c8daeb88f5d6", #get it from https://my.telegram.org/auth
    bot_token="5350336559:AAEn4QTVHUXDFhb-Aa3yAhqv-ap5MKz9nVQ", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
