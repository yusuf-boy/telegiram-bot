from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 📦 Mahsulotlar ro'yxati
products = {
    'model_a': {
        'name': "📱 MegaPhone X100",
        'desc': "🔋 6000mAh | 📸 108MP kamera | 💾 128GB xotira\n💰 Narxi: 2.500.000 so'm",
        'image': 'https://example.com/x100.jpg'
    },
    'model_b': {
        'name': "📱 LitePhone A30",
        'desc': "🔋 5000mAh | 📸 48MP kamera | 💾 64GB xotira\n💰 Narxi: 1.750.000 so'm",
        'image': 'https://example.com/a30.jpg'
    }
}

# 🔘 Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Mahsulotlar", callback_data='catalog')],
        [InlineKeyboardButton("📞 Bog‘lanish", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Xush kelibsiz!\n\nBu bizning rasmiy botimiz. Pastdagi menyudan tanlang:", reply_markup=reply_markup)

# 🔘 Tugmalarni boshqarish
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'catalog':
        keyboard = [
            [InlineKeyboardButton(products['model_a']['name'], callback_data='model_a')],
            [InlineKeyboardButton(products['model_b']['name'], callback_data='model_b')],
            [InlineKeyboardButton("⬅️ Ortga", callback_data='main_menu')]
        ]
        await query.edit_message_text("📦 Mahsulotlar ro‘yxati:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data in products:
        product = products[query.data]
        keyboard = [
            [InlineKeyboardButton("📲 Buyurtma berish", url='https://t.me/username')],
            [InlineKeyboardButton("⬅️ Mahsulotlarga qaytish", callback_data='catalog')]
        ]
        await query.message.reply_photo(
            photo=product['image'],
            caption=f"{product['name']}\n\n{product['desc']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == 'contact':
        await query.edit_message_text("📞 Bog‘lanish uchun:\n\n📱 Tel: +998 90 123-45-67\n📍 Ofis: Toshkent\n🌐 Web: www.mobilsanoat.uz")

    elif query.data == 'main_menu':
        await start(query, context)

# 🔁 Ishga tushirish
if __name__ == '__main__':
    app = ApplicationBuilder().token("BOT_TOKEN_BU_YERGA").build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Bot ishga tushdi.")
    app.run_polling()
