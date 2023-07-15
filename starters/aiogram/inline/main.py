from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.callback import menu_callback

menu_start = InlineKeyboardMarkup(row_width=1)
btn_good = InlineKeyboardButton(
    text=("🤗 Хорошо!"),
    callback_data=menu_callback.new(item_name="good"),
)
btn_bad = InlineKeyboardButton(
    text=("😡 Плохо("),
    callback_data=menu_callback.new(item_name="bad"),
)

menu_start.add(btn_good)
menu_start.add(btn_bad)
