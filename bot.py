import telebot
from telebot.types import Message







bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(func=lambda message: True)
#def upper(message: Message):
#    bot.reply_to(message, message.text.upper())

smiles = [':)',
          ':(',
          ]
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id !=661511672:
        bot.reply_to(message, 'привет')
    else:
        bot.reply_to(message, 'пока')
    pass          
          
#@bot.message_handler(commands=['start', 'help'])
#def upper(message: Message):
#    bot.reply_to(message, 'привет')
#    pass          
          

bot.polling()

