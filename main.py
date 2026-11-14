import asyncio

from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
)
from config.settings import BOT_TOKEN
# from handlers.users.abcreklama import rt as abcreklama

# from handlers.users.reklama import rt as reklama
from handlers.users.start import rt as start
# from handlers.users.test import rt as test
# from handlers.users.help import rt as help
# from handlers.users.cars import rt as cars
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)

    # dp.include_router(abcreklama)

    # dp.include_router(reklama)
    dp.include_router(start)
    # dp.include_router(bot)
    # dp.include_router(help)
    # dp.include_router(test)
    # dp.include_router(cars)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga ulang")
