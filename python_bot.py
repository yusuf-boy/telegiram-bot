import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from gtts import gTTS

# ======= TEST SAVOLLARI (Namuna) =======
questions = [
    {
        "question": "이것은 무엇입니까?",
        "options": ["A) 사과", "B) 바나나", "C) 포도", "D) 오렌지"],
        "answer": "A) 사과",
        "image": "apple.jpg",
        "tts": "이것은 무엇입니까?"
    },
    # Boshqa savollar shu yerga qo‘shiladi
]

user_progress = {}

# ======= TTS YARATISH =======
def create_voice(text, filename="question.mp3"):
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    return filename

# ======= START KOMANDASI =======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧪 Test", callback_data='start_test')],
        [InlineKeyboardButton("📘 Grammatika", callback_data='show_grammar')]
    ]
    await update.message.reply_text(
        "Assalomu alaykum! Quyidagilardan birini tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ======= TESTNI BOSHLASH =======
async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_progress[query.from_user.id] = 0
    await send_question(update, context)

# ======= SAVOLNI YUBORISH =======
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    index = user_progress.get(user_id, 0)

    if index >= len(questions):
        await update.callback_query.message.reply_text("✅ Test tugadi! Rahmat.")
        return

    q = questions[index]
    buttons = [
        [InlineKeyboardButton(opt, callback_data=f"answer|{opt}")] for opt in q['options']
    ]

    # Rasm yuborish
    if os.path.exists(q['image']):
        with open(q['image'], 'rb') as photo:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)

    # TTS yuborish
    voice_file = create_voice(q['tts'])
    with open(voice_file, 'rb') as audio:
        await context.bot.send_voice(chat_id=update.effective_chat.id, voice=audio)

    await update.callback_query.message.reply_text(q['question'], reply_markup=InlineKeyboardMarkup(buttons))

# ======= JAVOBNI TEKSHIRISH =======
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    index = user_progress.get(user_id, 0)
    q = questions[index]
    selected = query.data.split('|')[1]

    if selected == q['answer']:
        await query.message.reply_text("✅ To‘g‘ri javob!")
    else:
        await query.message.reply_text(f"❌ Noto‘g‘ri. To‘g‘ri javob: {q['answer']}")

    user_progress[user_id] += 1
    await send_question(update, context)

# ======= GRAMMATIKA BO‘LIMI =======
async def show_grammar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("📘 Grammatika darslari tez orada qo‘shiladi.")

# ======= BOTNI ISHGA TUSHIRISH =======
if __name__ == '__main__':
    app = ApplicationBuilder().token("8061266773:AAEKneALpb18B01bKlwqhbCFKSv7x38mGt8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start_test, pattern="start_test"))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern=r"^answer\|"))
    app.add_handler(CallbackQueryHandler(show_grammar, pattern="show_grammar"))
    app.add_handler(CallbackQueryHandler(handle_answer))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

