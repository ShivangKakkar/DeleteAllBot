import os
from pyrogram import Client
from pystark.config import API_ID, API_HASH

SESSION = os.environ.get('SESSION')


userbot = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)
