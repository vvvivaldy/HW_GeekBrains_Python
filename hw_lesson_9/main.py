import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('5976861589:AAEjN6b1tDlQLvJwVX7RiaiaP1UnDCA2z1Y')

step = randint(1,2) #далее: четное - игрок,нечетное - бот
candy = 221
move = randint(1,28)
starter = 0
winner = None
move_person =None
move_helper_hard = 0
@bot.message_handler(commands=['start','help','Помощь']) #объявляет реакции на команды
def start(message):
    bot.send_message(message.chat.id,''' 
    Взгляни на список комманд:
    /start - запуск бота
    /help - список команд
    /game - запуск игры
    /game_hard - запуск игры с умным ботом''')

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
        bot.send_message(message.chat.id,f'Сколько конфет ты возьмёшь?Но не более 28 и не менее 1!')
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
    but3 = types.KeyboardButton('/Перезапустить(обычный)')
    but4 = types.KeyboardButton('/Помощь')
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id,'Нажми кнопку', reply_markup=markup)

@bot.message_handler(commands=['game_hard','продолжить'])
def game_hard(message):
    global starter #работает исправно
    global step #рабоатет исправно, меняет вхождения как надо
    global candy #работает исправно
    global move #работает исправно
    global winner #рабоатет исправно
    global move_person
    global move_helper_hard
    if starter == 0:
        bot.send_message(message.chat.id,'Ну давай поиграем В ХАРД РЕЖИМ ;)') # отправляет сообщение
    if not step%2:
        if starter == 0:
            bot.send_message(message.chat.id,'Всего конфет 221\n\nТы ходишь первый!')
            starter = 1
        bot.send_message(message.chat.id,f'Сколько конфет ты возьмёшь?Но не более 28 и не менее 1!')
        bot.register_next_step_handler(message,go_hard) ### регистрирует то,что отправил пользователь.Первый аргумент - то,что передается как агумент в функцию, Второй аргумент - вызываемая ф-ция
        if winner == 1:
            return
    else:
        if starter == 0:
            bot.send_message(message.chat.id,'Всего конфет 221\n\nЯ хожу первый!')
            starter = 1
            move_helper_hard = 1
            move = 24
        if move_helper_hard==0:
            if move_person<24:
                move = 24-move_person
                move_helper_hard=1
            else:
                move = 24
                move_helper_hard=1
        elif candy>29 and candy<58:
            move = candy-29
        elif candy<29:
            move=candy
        elif candy in (range(58,86)):
            move = candy-58
        elif move_person != 28 and move_person!= None:
            move = 28-move_person
        elif move_person!=None:
            move = 28
        candy-=move
        if candy == 0:
            bot.send_message(message.chat.id,f'Я взял {move}\nОсталось конфет {candy}')
            bot.send_message(message.chat.id,f'Игра окончена! Победитель: Бот')
            return
        bot.send_message(message.chat.id,f'Я взял {move}\nОсталось конфет {candy}\nТеперь твой ход!')
        step+=1
        button_hard(message)

def button_hard(message): #работает как надо
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('/продолжить')
    but2 = types.KeyboardButton('/Закончить')
    but5 = types.KeyboardButton('/перезапустить(хард)')
    but4 = types.KeyboardButton('/Помощь')
    markup.add(but1)
    markup.add(but2)
    markup.add(but5)
    markup.add(but4)
    bot.send_message(message.chat.id,'Нажми кнопку', reply_markup=markup)

def go_hard(message): #работает
    global step,candy,winner,move_person
    move_person = int(message.text)
    candy -= move_person
    if candy == 0:
            bot.send_message(message.chat.id,f'Игра окончена! Победитель: Ты')
            winner = 1
            return
    bot.send_message(message.chat.id,f'Осталось конфет {candy}\nТеперь мой ход!')
    step+=1 
    if not step%2!=True:
        button_hard(message)

@bot.message_handler(commands=['Перезапустить(обычный)']) #рабоатет, но надо будет перепроверить после фикса основной части
def restart(message):
    bot.send_message(message.chat.id,'Перезапуск...')
    global step
    global candy
    global move
    global starter
    global winner
    global move_person
    global move_helper_hard
    move_helper_hard = 0
    move_person = None
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    starter = 0
    winner = None
    game(message)

@bot.message_handler(commands=['перезапустить(хард)']) #рабоатет, но надо будет перепроверить после фикса основной части
def restart(message):
    bot.send_message(message.chat.id,'Перезапуск...')
    global step
    global candy
    global move
    global starter
    global winner
    global move_person
    global move_helper_hard
    move_helper_hard = 0
    move_person = None
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    starter = 0
    winner = None
    game_hard(message)

@bot.message_handler(commands=['Закончить'])
def end(message):
    global step
    global candy
    global move
    global starter
    global winner
    global move_person
    global move_helper_hard
    move_helper_hard = 0
    move_person = None
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    starter = 0
    winner = None
    bot.send_message(message.chat.id,'Игра окончена!')


bot.infinity_polling()