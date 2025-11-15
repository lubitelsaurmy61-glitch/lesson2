from bot_logic import *
import time, threading, schedule, requests
import telebot

bot = telebot.TeleBot("8203518338:AAHbg-teUaEwBNPlNYny4df9Be41yiXNzjc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['pass'])    
def send_password(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Сгенерированный пароль: {password}")
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '''📄 <b>Вот команды, которые обрабатывает этот бот:</b>

"/start" — Запуск бота;
"/hello" — Приветствие;
"/pass" — Генерадция рандомного пароля;
"/bye" — Прощяние;
"/help" — Вывод списка команд.''', parse_mode='html')

@bot.message_handler(commands=['timer'])
def send_welcome(message):
    bot.reply_to(message, "Используйте /set <секунды>, чтобы установить таймер.")


def beep(chat_id) -> None:
    """Отправляю звуковое сообщение."""
    bot.send_message(chat_id, text='Бип!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Используйте: /set <секунды>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)
    
@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи: {emodji}")
    
@bot.message_handler(commands=['random_number'])
def rn(message):
    rand_n = random.randint(0, 100)
    bot.reply_to(message, f'Рандомное число: {rand_n}')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
