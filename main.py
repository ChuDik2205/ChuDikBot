import asyncio
import logging, sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from datetime import datetime
from config import config
from modes import spy, dolbaeb

dp = Dispatcher()

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    dp.include_routers(spy.router, dolbaeb.router)
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await bot.close()


if __name__ == "__main__":
    print("bot start")
    asyncio.run(main())


