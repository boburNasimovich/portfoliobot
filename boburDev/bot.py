from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8569428439:AAGJZej_veb_gWJj9ty5dBQ6LiyX0hb0s_Q"  # Tokeningizni shu yerga qo'ying


# 🔹 Asosiy menyu (funksiya shaklida, qayta ishlatamiz)
def main_menu():
    keyboard = [
        [InlineKeyboardButton("> Men haqimda", callback_data="about")],
        [InlineKeyboardButton("> Portfolio", callback_data="portfolio")],
        [InlineKeyboardButton("> Aloqa", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)


# 🔹 /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bobur @nsmvch ning portfolio boti.\nQuyidagilardan birini tanlang:",
        reply_markup=main_menu()
    )


# 🔹 Tugma bosilganda ishlovchi funksiya
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        text = (
            "👋 Salom! Men Bobur — middle darajadagi Python dasturchiman.\n"
            "Telegram botlar, web loyihalar va avtomatlashtirish tizimlarini yarataman.\n\n"
            "🧠 Texnologiyalar: Python, HTML, CSS, JS, Tailwind, React, TS, Telegram API"
        )
        keyboard = [[InlineKeyboardButton("< Ortga", callback_data="back")]]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "portfolio":
        text = (
            "💼 Mening loyihalarim:\n\n"
            "1 Restoran buyurtma bot 🍔 @exampleburger_bot\n"
            "2 Kurslar uchun ro‘yxat bot 🎓 @examplereception_bot\n"
            "3 AI yordamida javob beruvchi bot 🤖 @exampleAI_bot\n\n"
        )
        keyboard = [[InlineKeyboardButton("< Ortga", callback_data="back")]]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "contact":
        text = (
            "📞 Aloqa ma'lumotlarim:\n\n"
            "📧 Email: boburnasimovich@gmail.com\n"
            "💬 Telegram: @nsmvch\n"
            "🌐 GitHub: github.com/boburNasimovich"
        )
        keyboard = [[InlineKeyboardButton("< Ortga", callback_data="back")]]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back":
        # Asosiy menyuga qaytish
        await query.edit_message_text(
            text="Asosiy menyu ⬇️",
            reply_markup=main_menu()
        )


# 🔹 Botni ishga tushurish
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Portfolio bot ishga tushdi 🚀")
app.run_polling()
