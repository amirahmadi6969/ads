from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
import requests

TOKEN = "7018830857:AAE04BaK67RskmJJAAgJ5h_7h9IJntKcav8"
API_URL = "https://hafez-dxle.onrender.com"

ABOUT_TEXT = """✨ سلام رفیق! 👋  
من یه ربات همه‌فن‌حریفم! 🤖  
هرچی بخوای دارم:  
📚 دانستنی، 🎭 داستان، 🎬 دیالوگ، 🎤 جوک، 📖 شعر، 🎴 فال حافظ و کلی چیز دیگه!

👇 فقط یکی از دکمه‌ها رو بزن و کیف کن!
"""


def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🧠 دانستنی باحال", callback_data='get_fact')],
        [InlineKeyboardButton("📖 داستان کوتاه", callback_data='get_fact_2')],
        [InlineKeyboardButton("🎬 دیالوگ ماندگار", callback_data='get_fact_3')],
        [InlineKeyboardButton("📜 فال حافظ (تصادفی)", callback_data='fal')],
        [InlineKeyboardButton("🤣 بخندیم؟ (جوک)", callback_data='jok')],
        [InlineKeyboardButton("📝 شعر از سعدی", callback_data='sa')],
        [InlineKeyboardButton("📅 مناسبت امروز", callback_data='mo')],
        [InlineKeyboardButton("📌 بیو کانال", callback_data='bi')],
        [InlineKeyboardButton("🧩 چیستان باحال", callback_data='chi')],
        [InlineKeyboardButton("💬 حدیث از بزرگان", callback_data='ha')]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_fact():
    try:
        response = requests.get('https://api.codebazan.ir/danestani/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت دانستنی."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_2():
    try:
        response = requests.get('https://api.codebazan.ir/dastan')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت داستان."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_3():
    try:
        response = requests.get('https://api.codebazan.ir/dialog')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت دیالوگ."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_4():
    try:
        response = requests.get('https://api.codebazan.ir/jok/pa-na-pa/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت جوک."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_5():
    try:
        response = requests.get('https://api.codebazan.ir/jok/khatere/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت جوک."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_6():
    try:
        response = requests.get('https://api.codebazan.ir/jok/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت جوک."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_7():
    try:
        response = requests.get('https://api.codebazan.ir/ghazalsaadi/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت شعر."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_8():
    try:
        response = requests.get('https://api.codebazan.ir/hadith/?type=random_html')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت حدیث بزرگان."
    except:
        return "❌ ارتباط برقرار نشد."

def get_fact_9():
    try:
        response = requests.get('https://api.codebazan.ir/monasebat/')
        if response.status_code == 200:
            lines = response.text.strip().split('\n')
            return [{"occasion": line.strip()} for line in lines if line.strip()]
        else:
            return [{"occasion": "❌ خطا در دریافت مناسبت‌ها."}]
    except:
        return [{"occasion": "❌ ارتباط برقرار نشد."}]

def get_fact_10():
    try:
        response = requests.get('https://api.codebazan.ir/bio/')
        return response.text.strip() if response.status_code == 200 else "❌ خطا در دریافت حدیث بزرگان."
    except:
        return "❌ ارتباط برقرار نشد."

import random

def get_fact_11():
    try:
        response = requests.get('https://api.codebazan.ir/chistan/')
        if response.status_code == 200:
            data = response.json()
            return data.get("Result", [])
        else:
            return [{"soal": "❌ خطا در دریافت چیستان‌ها.", "javab": ""}]
    except:
        return [{"soal": "❌ ارتباط برقرار نشد.", "javab": ""}]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT, reply_markup=get_main_keyboard())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👇 یکی از گزینه‌های خوشگل زیر رو بزن، چیزی جذاب در انتظارتِ!", reply_markup=get_main_keyboard())


async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    reply_markup = get_main_keyboard()

    if data == 'get_fact':
        fact = get_fact()
        await query.message.reply_text(f"📘 دانستنی:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'get_fact_2':
        fact = get_fact_2()
        await query.message.reply_text(f"📘 داستان کوتاه:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'get_fact_3':
        fact = get_fact_3()
        await query.message.reply_text(f"🎬 دیالوگ:\n\n{fact}", reply_markup=reply_markup)
    
    elif data == 'sa':
        fact = get_fact_7()
        await query.message.reply_text(f"🎬 شعر:\n\n{fact}", reply_markup=reply_markup)
    
    elif data == 'ha':
        fact = get_fact_8()
        await query.message.reply_text(f"🎬 حدیث بزرگان:\n\n{fact}", reply_markup=reply_markup)
    
    elif data == 'mo':
        fact = get_fact_9()
        await query.message.reply_text(f"🎬 مناسبت امروز:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'bi':
        fact = get_fact_10()
        await query.message.reply_text(f"🎬  بیوگرافی کانال:\n\n{fact}", reply_markup=reply_markup)
    
    elif data == 'chi':
        chistans = get_fact_11()
        if chistans and isinstance(chistans, list):
            chi = random.choice(chistans)  # انتخاب رندوم یک چیستان
            soal = chi.get("soal", "❓ بدون سوال")
            javab = chi.get("javab", "❌ پاسخ موجود نیست.")
            msg = f"❓ چیستان:\n\n{soal}\n\n🔑 پاسخ: {javab}"
            await query.message.reply_text(msg, reply_markup=reply_markup)
        else:
            await query.message.reply_text("❌ خطا در دریافت چیستان.", reply_markup=reply_markup)



    elif data == 'jok':
        jok_keyboard = [
            [InlineKeyboardButton("🤣 جوک پا نا پا", callback_data='jok_1')],
            [InlineKeyboardButton("🔥 جوک خطرناک", callback_data='jok_2')],
            [InlineKeyboardButton("😄 جوک ساده و باحال", callback_data='jok_3')]
                ]

        await query.message.reply_text("😄 یک نوع جوک انتخاب کن:", reply_markup=InlineKeyboardMarkup(jok_keyboard))

    elif data == 'jok_1':
        fact = get_fact_4()
        await query.message.reply_text(f"😂 جوک پا نا پا:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'jok_2':
        fact = get_fact_5()
        await query.message.reply_text(f"😂 جوک خطر:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'jok_3':
        fact = get_fact_6()
        await query.message.reply_text(f"😂 جوک ساده:\n\n{fact}", reply_markup=reply_markup)

    elif data == 'fal':
        try:
            response = requests.get(f"{API_URL}/fal")
            item = response.json()
            msg = f"📖 *{item['title']}*\n\n_{item['interpreter']}_"
            await query.message.reply_text(msg, parse_mode="Markdown", reply_markup=reply_markup)
        except:
            await query.message.reply_text("❌ خطا در دریافت فال.", reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("ربات فعال شد.")
    app.run_polling()

if __name__ == '__main__':
    main()
