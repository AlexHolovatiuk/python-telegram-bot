from fileinput import filename

import telebot

token = '7636094498:AAFlezEInLwscQvSYtBHzlWmVcwEKjyVoEo'
bot = telebot.TeleBot(token)
filename = "bot_message.txt"

@bot.message_handler(content_types=['text'])
def is_text(message):
    with open(filename, 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'Збережено до файла')


if __name__ == '__main__':
    bot.polling()