import os
from pyrogram import Client

SESSION = os.environ.get('SESSION')


userbot = Client(
    SESSION,
    api_id=int(os.environ.get('API_ID')),
    api_hash=os.environ.get("API_HASH")
)
