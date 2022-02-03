from telethon.sync import TelegramClient
from telethon import functions


def get_all_chats(api_id: int, api_hash: str):
    with TelegramClient("session_name", api_id, api_hash) as client:
        result = client(functions.messages.GetAllChatsRequest(except_ids=[42]))
        with open("chats.txt", "w") as file:
            chats = ""
            for chat in result.to_dict()["chats"]:
                chats = f'{chats}\nTitle: {chat["title"]}\nID: {chat["id"]}\n'
            file.write(chats)
