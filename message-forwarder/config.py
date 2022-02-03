import os

import dotenv

dotenv.load_dotenv()


API_ID: int = int(os.getenv("API_ID", 0))
API_HASH: str = os.getenv("API_HASH", "")

FROM_CHAT_ID: int = int(os.getenv("FROM_CHAT_ID", 0))
TARGET_USER_ID: int = int(os.getenv("TARGET_USER_ID", 0))
TO_CHAT_ID: int = int(os.getenv("TO_CHAT_ID", 0))
