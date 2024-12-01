import asyncio
import logging, sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from datetime import datetime
from config import config
from modes import spy, dolbaeb

dp = Dispatcher()
mode_dolbaeb = False
mode_spy = False

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'')


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


