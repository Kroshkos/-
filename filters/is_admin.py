from typing import Any, List

from aiogram.filters import BaseFilter
from aiogram.types import Message
import sqlite3
class IsAdmin(BaseFilter):

    def __init__(self, user_ids: int | List[int]) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        conn = sqlite3.connect('main.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE id = ?", (message.from_user.id,))
        accounts = cursor.fetchone()
        conn.commit()
        conn.close()
        if accounts is not None:
            result = 1
        else:
            result = 0

        if isinstance(self.user_ids, int):
            return result == self.user_ids