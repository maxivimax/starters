from aiogram import types
from __main__ import dp
from messages.main import MESSAGES
from inline.main import menu_start
from callback.callback import menu_callback


@dp.message_handler(commands=["start"], state="*")
async def bot_start(message: types.Message):
    await message.answer(
        MESSAGES["start"](), reply_markup=menu_start, parse_mode="HTML"
    )


@dp.callback_query_handler(menu_callback.filter(item_name="good"), state="*")
async def bot_good(call: types.CallbackQuery):
    await call.message.delete()
    await call.bot.send_message(
        call.message.chat.id,
        MESSAGES["good"](),
        parse_mode="HTML",
    )

@dp.callback_query_handler(menu_callback.filter(item_name="bad"), state="*")
async def bot_bad(call: types.CallbackQuery):
    await call.message.delete()
    await call.bot.send_message(
        call.message.chat.id,
        MESSAGES["bad"](),
        parse_mode="HTML",
    )

