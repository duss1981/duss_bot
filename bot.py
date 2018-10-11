import telebot

import socket
import threading
import sys


from telebot.types import Message
from telebot import apihelper





TOKEN='bot683788474:AAEAxCJ_44yCLDP6exQkqfvPe68yijAnpys'
#PROXY='socks5://userproxy:password@https://'
#PROXY='socks5://socks5_user:socks_pass@https://195.14.114.123:4145'
#PROXY='socks5://47.88.26.87:1080'
PROXY='46.101.215.222:8118'

apihelper.proxy = {'http':PROXY}
#apihelper.proxy = {'https':PROXY}
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

