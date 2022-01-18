from telethon import TelegramClient
from telethon.events import NewMessage

from config import Config

client = TelegramClient("session_name", Config.API_ID, Config.API_HASH)


@client.on(NewMessage(chats=Config.FROM_CHAT_ID, from_users=Config.TARGET_USER_ID))
async def main(event):
    await event.forward_to(Config.TO_CHAT_ID)


if __name__ == "__main__":
    client.start()
    client.run_until_disconnected()
