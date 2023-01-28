import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('5976861589:AAEjN6b1tDlQLvJwVX7RiaiaP1UnDCA2z1Y')

step = randint(1,2) #далее: четное - игрок,нечетное - бот
candy = 221
move = randint(1,28)
a = 0
next = "Продолжить"


@bot.message_handler(commands=['start','help']) #объявляет реакции на команды
def start(message):
    bot.send_message(message.chat.id,''' 
    Взгляни на список комманд:
    /start - запуск бота
    /help - список команд
    /game - запуск игры
    /restart - перезапускает игру
    /end - заканчивает игру''')

@bot.message_handler(commands=['game'])
def game(message):
    global a #работает исправно
    global step #рабоатет исправно, меняет вхождения как надо
    global candy #работает исправно
    global move #работает исправно
    global next # нихуя не рабоает,че за пиздец

    if a == 0:
        bot.send_message(message.chat.id,'Ну давай поиграем ;)') # отправляет сообщение
    while candy>0:
        step+=1
        if next == 'Продолжить':
            if not step%2:
                if a == 0:
                    bot.send_message(message.chat.id,'Всего конфет 221\n\nТы ходишь первый!')
                    a = 1
                    print(8)
                bot.send_message(message.chat.id,f'Сколько конфет ты возьмёшь?Но не более 28!')
                bot.register_next_step_handler(message,go) ### регистрирует то,что отправил пользователь.Первый аргумент - то,что передается как агумент в функцию, Второй аргумент - вызываемая ф-ция
                bot.register_next_step_handler(message,next_move)
                bot.send_message(message.chat.id,f'Осталось конфет {candy}\nТеперь мой ход!')
                print(next,1)
            else:
                if a == 0:
                    bot.send_message(message.chat.id,'Всего конфет 221\n\nЯ хожу первый!')
                    a = 1
                move = randint(1,28)
                candy-=move
                bot.send_message(message.chat.id,f'Я взял {move}\nОсталось конфет {candy}\nТеперь твой ход!')
                print(next,0)
        elif next == 'Закончить':
            return
        else:
            continue

def next_move(message):
    global next
    next = message.text

def go(message): #в душе не ебу работает,или нет. Вроде бы да
    global step,candy,next
    move_person = int(message.text)
    candy -= move_person
    #bot.send_message(message.chat.id,f'Осталось конфет {candy}\nТеперь мой ход!')
    print(step)
    if not step%2!=True:
        button(message)
        print(123)


def button(message): #работает как надо
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Продолжить')
    but2 = types.KeyboardButton('Закончить')
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,'Нажми кнопку', reply_markup=markup)


@bot.message_handler(commands=['restart']) #рабоатет, но надо будет перепроверить после фикса основной части
def restart(message):
    bot.send_message(message.chat.id,'Перезапуск...')
    global step
    global candy
    global move
    global a
    step = randint(1,2) 
    candy = 221
    move = randint(1,28)
    a = 0
    game(message)

# @bot.message_handler(commands=['end'])
# def end(message):
#     bot.send_message(message.chat.id,'Игра окончена!')
















bot.infinity_polling()