import os
import telebot
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response['choices'][0]['message']['content'])
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

print("🤖 Bot is running...")
bot.polling()
