import sys

from telethon import TelegramClient
from telethon.events import NewMessage

from config import API_ID, API_HASH, FROM_CHAT_ID, TARGET_USER_ID, TO_CHAT_ID
from generate import get_all_chats

if "generate" in sys.argv:
    get_all_chats(API_ID, API_HASH)
    exit()

client = TelegramClient("session_name", API_ID, API_HASH)


@client.on(NewMessage(chats=FROM_CHAT_ID, from_users=TARGET_USER_ID if TARGET_USER_ID else None))
async def main(event):
    await event.forward_to(TO_CHAT_ID)


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
