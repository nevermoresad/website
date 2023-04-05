
from aiogram.bot import Bot
from aiogram.types import ParseMode


bot = Bot(token="6039482612:AAGuCtJK_QqsmLemFv7oC49l50MLhoiryFw")


async def send_data(**kwargs):
    await bot.send_message(chat_id=1359376273,
                           text="🔔 <b>Новое резюме</b>\n\n"
                                f"👤 <b>Имя и фамилия:</b> <i>{kwargs['name']}</i>\n"
                                f"🧩 <b>Возраст:</b> <i>{kwargs['age']}</i>\n"
                                f"💼 <b>Навык:</b> <i>{kwargs['skill']}</i>\n"
                                f"🏆 <b>Стаж:</b> <i>{kwargs['stage']}</i>\n"
                                f"🌉 <b>О себе:</b> <i>{kwargs['desc']}</i>\n"
                                f"📨 <b>Email:</b> <i>{kwargs['email']}</i>\n",
                           parse_mode=ParseMode.HTML)
