import telebot

import cloud

bot = telebot.TeleBot("1400405054:AAFo1D6ahC_Nl56Y6a_N_vupY31Okd6KD9s")

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Получить текущие данные')
keyboard1.row('Показать температуру', 'Установить температуру')
keyboard1.row('Показать влажность воздуха', 'Установить влажность воздуха')
keyboard1.row('Показать уровень освещенности', 'Установить уровень освещенности')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Назад')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Соединение с умной теплицей установлено!')
    bot.send_message(message.chat.id, 'Вы можете начинать управлять системой...', reply_markup=keyboard1)
    

@bot.message_handler(content_types=['text'])
def comands(message):
    if message.text == 'Получить текущие данные':
        text = "Текущие данные: {0}".format(cloud.get_current_data())
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
    elif message.text == 'Показать температуру':
        text = "Текущая температура: {0}".format(cloud.get_current_temperature())
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
    elif message.text == 'Показать влажность воздуха':
        text = "Текущая влажность: {0}".format(cloud.get_current_humidity_air())
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
    elif message.text == 'Показать уровень освещенности':
        text = "Текущая влажность: {0}".format(cloud.get_current_brightness_level())
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
    elif message.text == 'Установить температуру':
        msg = bot.reply_to(message, "Введите необходимую температуру")
        bot.register_next_step_handler(msg, SET_TEMPERATURE)
    elif message.text == 'Установить влажность воздуха':
        msg = bot.reply_to(message, "Введите необходимую влажность воздуха")
        bot.register_next_step_handler(msg, SET_HUMIDITY)
    elif message.text == 'Установить уровень освещенности':
        msg = bot.reply_to(message, "Введите необходимый уровень освещенности")
        bot.register_next_step_handler(msg, SET_HUMIDITY)
        
        

def SET_TEMPERATURE(message):
    value = message.text
    cloud.set_temperature(value)
    bot.send_message(message.chat.id, 'Температура установлена!', reply_markup=keyboard1)

def SET_HUMIDITY(message):
    value = message.text
    cloud.set_humidity_air(value)
    bot.send_message(message.chat.id, 'Влажность установлена!', reply_markup=keyboard1)


def SET_BRIGHTNESS(message):
    value = message.text
    cloud.set__brightness_level(value)
    bot.send_message(message.chat.id, 'Освещенность установлена!', reply_markup=keyboard1)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)