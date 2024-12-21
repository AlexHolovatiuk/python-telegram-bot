from fileinput import filename

import telebot

token = '7636094498:AAFlezEInLwscQvSYtBHzlWmVcwEKjyVoEo'
bot = telebot.TeleBot(token)

file_text = "bot_text.txt"
file_number = "bot_number.txt"

@bot.message_handler(content_types=['text'])
def is_text(message):
    if message.text:
        file_text = "bot_text.txt"
    else:
        file_number = "bot_number.txt"

    with open(filename, 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'Збережено до файла')


if __name__ == '__main__':
    bot.polling()