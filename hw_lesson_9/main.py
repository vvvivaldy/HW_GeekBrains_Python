import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('5976861589:AAEjN6b1tDlQLvJwVX7RiaiaP1UnDCA2z1Y')

step = randint(1,2) #далее: четное - игрок,нечетное - бот
candy = 221
move = randint(1,28)
starter = 0
winner = None

@bot.message_handler(commands=['start','help','Помощь']) #объявляет реакции на команды
def start(message):
    bot.send_message(message.chat.id,''' 
    Взгляни на список комманд:
    /start - запуск бота
    /help - список команд
    /game - запуск игры''')

@bot.message_handler(commands=['game','Продолжить'])
def game(message):
    global starter #работает исправно
    global step #рабоатет исправно, меняет вхождения как надо
    global candy #работает исправно
    global move #работает исправно
    global winner #рабоатет исправно

    if starter == 0:
        bot.send_message(message.chat.id,'Ну давай поиграем ;)') # отправляет сообщение
    if not step%2:
        if starter == 0:
            bot.send_message(message.chat.id,'Всего конфет 221\n\nТы ходишь первый!')
            starter = 1
        bot.send_message(message.chat.id,f'Сколько конфет ты возьмёшь?Но не более 28!')
        bot.register_next_step_handler(message,go) ### регистрирует то,что отправил пользователь.Первый аргумент - то,что передается как агумент в функцию, Второй аргумент - вызываемая ф-ция
        if winner == 1:
            return
    else:
        if starter == 0:
            bot.send_message(message.chat.id,'Всего конфет 221\n\nЯ хожу первый!')
            starter = 1
        if candy>28:
            move = randint(1,28)
        else:
            move = randint(1,candy)
        candy-=move
        if candy == 0:
            bot.send_message(message.chat.id,f'Я взял {move}\nОсталось конфет {candy}')
            bot.send_message(message.chat.id,f'Игра окончена! Победитель: Бот')
            return
        bot.send_message(message.chat.id,f'Я взял {move}\nОсталось конфет {candy}\nТеперь твой ход!')
        step+=1
        button(message)



def go(message): #работает
    global step,candy,winner
    move_person = int(message.text)
    candy -= move_person
    if candy == 0:
            bot.send_message(message.chat.id,f'Игра окончена! Победитель: Ты')
            winner = 1
            return
    bot.send_message(message.chat.id,f'Осталось конфет {candy}\nТеперь мой ход!')
    step+=1 
    if not step%2!=True:
        button(message)


def button(message): #работает как надо
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('/Продолжить')
    but2 = types.KeyboardButton('/Закончить')
    but3 = types.KeyboardButton('/Перезапустить')
    but4 = types.KeyboardButton('/Помощь')
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id,'Нажми кнопку', reply_markup=markup)


@bot.message_handler(commands=['Перезапустить']) #рабоатет, но надо будет перепроверить после фикса основной части
def restart(message):
    bot.send_message(message.chat.id,'Перезапуск...')
    global step
    global candy
    global move
    global starter
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    starter = 0
    game(message)

@bot.message_handler(commands=['Закончить'])
def end(message):
    global step
    global candy
    global move
    global starter
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    starter = 0
    bot.send_message(message.chat.id,'Игра окончена!')
















bot.infinity_polling()