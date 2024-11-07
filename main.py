import asyncio
from aiogram import Bot, Dispatcher

from handlers import bot_messages, user_commands, questionaire_vshp, questionaire_zargor
from callbacks import pagination
from middlewares.chekc_sub import CheckSubscription

async def main():
    
    bot = Bot("6265878181:AAGXfPN5SDN3W5UIPX0D3W8b_HylWO9ztlk")
    dp = Dispatcher()

    dp.message.middleware(CheckSubscription())

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire_vshp.router,
        questionaire_zargor.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())