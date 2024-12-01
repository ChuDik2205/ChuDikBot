from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "пип")
async def message_with_text(message: Message):
    await message.answer("шпион тест!")