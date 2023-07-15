from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import API_TOKEN, ADMIN_API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

admin_bot = Bot(token=ADMIN_API_TOKEN)
admin_dp = Dispatcher(admin_bot, storage=MemoryStorage())


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Старт"),
        ]
    )


async def startup(dp: Dispatcher):
    msg = f"Bot started"
    await set_default_commands(dp)
    print(msg)


async def shutdown(dp: Dispatcher):
    msg = f"Bot stopped"
    print(msg)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
    from handlers import dp

    executor.start_polling(
        dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True
    )
