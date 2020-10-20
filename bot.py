#it's bot

import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

# обработчик текстовых сообщений
#@bot.message_handler(content_types=["text"])
#def repeat_all_messages(message): # Название функции не играет никакой роли
#    bot.send_message(message.chat.id, message.text + " :)")
	
	
@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="кнопочка", url="https://i.pinimg.com/originals/97/ac/4a/97ac4a118931d7a0f88476535d76c308.jpg")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "нажми на кнопку.", reply_markup=keyboard)
	

# обработчик команды /start
#@bot.message_handler(commands=["start"])
#TODO


# запуск бесконечного цикла для получения новых записей; long polling
if __name__ == '__main__':
    bot.infinity_polling()
	
	
	


