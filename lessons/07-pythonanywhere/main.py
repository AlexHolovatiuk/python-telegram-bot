import telebot

token = '7636094498:AAFlezEInLwscQvSYtBHzlWmVcwEKjyVoEo'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def is_text(message):
    bot.send_message(message.chat.id, message.text + '\n[Бот працює]')


if __name__ == '__main__':
    bot.polling()
