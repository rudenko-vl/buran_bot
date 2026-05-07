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

# from openai import OpenAI
# from config import BOT_TOKEN, OPENAI_API_KEY

from config import BOT_TOKEN
import random

# client = OpenAI(api_key=OPENAI_API_KEY)

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

    # keyboard = [
    #     ["AI 🤖", "Мем 😂"],
    #     ["Roast 🔥", "Игра 🎮"],
    #     ["Факт 🧠"],
    # ]
    
    keyboard = [
        ["Игра 🎮"],
        ["Факт 🧠"],
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


# AI ответ
# async def ask_ai(text):

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "Ты веселый Telegram-бот. "
#                     "Отвечай кратко, смешно и дружелюбно."
#                 ),
#             },
#             {
#                 "role": "user",
#                 "content": text,
#             },
#         ],
#         max_tokens=150,
#     )

#     return response.choices[0].message.content


# Обработка сообщений
async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id

    # AI
    # if text == "AI 🤖":

    #     await update.message.reply_text(
    #         "Напиши мне любой вопрос 😎"
    #     )

    #     context.user_data["ai_mode"] = True
    #     return

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
    if text == "Факт 🧠":

        facts = [
            "У осьминога 3 сердца 🐙",
            "Банан — это ягода 🍌",
            "Арахис — это не орех 🥜",
            "У пчел пять глаз 🐝",
            "У акул нет ни одной кости 🦈",
            "На Венере день длится дольше, чем год 👽",
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

    # AI режим
    # elif context.user_data.get("ai_mode"):

    #     await update.message.reply_text(
    #         "Думаю... 🤔"
    #     )

    #     answer = await ask_ai(text)

    #     await update.message.reply_text(answer)

    # else:

    #     await update.message.reply_text(
    #         "Я тебя не понял 🤖"
    #     )


# Запуск
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT, messages)
)

print("Бот запущен 😎")

app.run_polling()