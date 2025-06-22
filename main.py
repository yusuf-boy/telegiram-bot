from translate import translate
import telebot

TOKEN = '8061266773:AAEKneALpb18B01bKlwqhbCFKSv7x38mGt8'
bot = telebot.TeleBot(token=TOKEN)

# /start komandasi uchun
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "🇺🇿 Assalomu alaykum!\n✍️ Matn yuboring, men uni tarjima qilaman.")

# Matn kelganda
@bot.message_handler(func=lambda message: True)
def translate_handler(message):
    original_text = message.text
    translated_text = translate(original_text)
    bot.reply_to(message, f"🔁 Tarjima:\n{translated_text}")

# Botni ishga tushirish
bot.polling()