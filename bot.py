from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
import random

# Хранилище игры
games = {}

# Мемы
# memes = [
#     "Когда пофиксил баг и появилось еще 5 😎",
#     "Работает — не трогай.",
#     "Я не опаздываю. Я оптимизирую ожидание.",
#     "99% программистов гуглят элементарные вещи.",
# ]

# Roast фразы
# buran = [
#     "Как открыть Буран? Если не знаешь, то лучше не открывай! 😁",
#     "Помни: Буран не тормозит, он просто дает тебе время подумать",
#     "Ты не ленивый. Ты async.",
# ]


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["Игра 🎮"],
        ["Факт про Буран 🖥️"],
    ]

    markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Йо 😎 Я мультибот.\nВыбирай режим.",
        reply_markup=markup
    )


# Игра
async def start_game(update: Update):

    user_id = update.message.from_user.id
    games[user_id] = random.randint(1, 10)

    await update.message.reply_text(
        "Я загадал число от 1 до 10 😈"
    )

# Обработка сообщений
async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id

    # Мем
    # elif text == "Мем 😂":

    #     await update.message.reply_text(
    #         random.choice(memes)
    #     )

    # Roast
    # elif text == "Buran 🔥":

    #     await update.message.reply_text(
    #         random.choice(buran)
    #     )

    # Факт
    if text == ("Факт про Буран 🖥️"
                ):

        facts = [
            "Программа «Буран» называется не в честь орбитального корабля",
            "Программу «Буран» не использовали при полетах в космос",
            "У программы есть скрытые функции, о которых никто не знает",
            "Если вы переместили товар в базе, а он не переместился физически — значит, у вас старая версия реальности",
            "«Буран» никогда не тормозит. Он просто дает вам время подумать",
        ]

        await update.message.reply_text(
            random.choice(facts)
        )

    # Игра
    elif text == "Игра 🎮":

        await start_game(update)

    # Проверка игры
    elif user_id in games:

        if text.isdigit():

            number = int(text)

            if number == games[user_id]:

                await update.message.reply_text(
                    "🔥 Ты угадал!"
                )

                del games[user_id]

            else:

                await update.message.reply_text(
                    "Неа 😁 Попробуй еще."
                )

# Запуск
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT, messages)
)

print("Бот запущен 😎")

app.run_polling()