from aiogram import Router, F, types, Bot
from aiogram.types import Message
from aiogram.filters.command import Command
router = Router()

from config import config
bot = Bot(token=config.bot_token.get_secret_value())


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Привет ЧОРТ --- {message.from_user.username}')


@router.message(Command("stop"))
async def cmd_stop(message: types.Message):

    await message.answer(f'Ах ты ЧОРТ ебаанн....')
    print("bot stop")
    await message.answer(f'А хуй тебе')


@router.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"инфа для гандона(ов):\nСеанс начался {started_at}")


@router.message(F.photo)
async def get_file(message: types.Message, bot: Bot):
    await message.answer("ОГОООООООО")
    await message.answer("ГАНДОН ОТПРАВИЛ МНЕ ФОТО!вкпРАПВРАПВпавправрТРАПВР")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path)


@router.message(F.text == 'ЧМО')
async def chmo(message: types.Message, bot: Bot):
    await message.answer("САМ ЧМО!!!")


@router.message(F.text == '777')
async def secret(message: types.Message):
    await message.answer_photo("https://i.ytimg.com/vi/7aPXGmPbyao/maxresdefault.jpg")


@router.message(F.text == 'ноу ноу ноу мистер фиш!')
async def nou(message: types.Message):
    await message.answer("ноу ноу....")
    await message.reply("эээ, ахуел ЧОРТ ебанный")


@router.message()
async def echo(message: types.Message, bot: Bot):

    try:
        print(message.text)
        await message.answer("ноу ноу ноу мистер фиш!")
    except TypeError:
        await message.answer("ноу ноу ноу мистер фиш!")

router.message.register(cmd_stop, Command("stop"))