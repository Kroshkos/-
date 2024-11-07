from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware

from aiogram.types import Message, TelegramObject

from keyboards.inline import sub_channel

class CheckSubscription(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
            event: Message, 
            data: Dict[str, Any]
            ) -> Any:
        chat_member = await event.bot.get_chat_member("-1001767214732", event.from_user.id)

        if chat_member.status == "left":
            await event.answer(
                "Подпишись на канал, чтоб быть в курсе всех событий и пользоваться ботом!\n\nЕсли вы подписались нажмити /start",
                reply_markup = sub_channel
            )
        else:
            return await handler(event, data)
        