from input import *
def to_str():
    global processed_line
    string = ''.join(processed_line)
    return string

def open_file(string):
    with open('справочник.txt','a') as data:
        data.write(string + '\n')

def add_id():
    global processed_line
    data = open('справочник.txt','r')
    last = data.readlines()
    data.close
    indexes = [i for i,c in enumerate(last) if c==';']
    if len(indexes)>0:
        processed_line.append(f';{indexes[-1]}')
    else:
        processed_line.append(';1')
            
            
update = lambda x: x.clear()
    
def operation():
    return int(input('Выберите действие (1 - записать контакт в справочник),(0 - показать все данные справочника): '))


def create_file():
    with open('справочник.txt','w') as data:
        data.write('Добро пожаловать в телефонный справочник!\n')






