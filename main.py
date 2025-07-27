import os
import telebot
import openai

# Load API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(func=lambda message: True)
def ai_chat(message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"⚠️ Error: {e}")

print("🤖 Bot is running...")
bot.polling()
