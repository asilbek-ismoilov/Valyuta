from aiogram.types import Message
from loader import dp
from aiogram import F
from valyuta import get_val_malum

@dp.message(F.text)
async def valyuta(message:Message):
    text = message.text
    natija = get_val_malum(text)
    await message.answer(natija)