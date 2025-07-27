import os
import openai
import telebot

# Load keys from environment variables
openai.api_key = os.getenv("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")
bot = telebot.TeleBot(os.getenv("8100670858:AAFXWNxycdRZllTCpDp6PTs23fU20SvKhAo"))

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
