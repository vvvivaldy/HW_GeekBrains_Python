from input import *
def to_str():
    global processed_line
    string = ''.join(processed_line)
    return string

def open_file(string):
    with open('hw_lesson_7/справочник.txt','a') as data:
        data.write(string + '\n')

def add_id():
    global processed_line
    data = open('hw_lesson_7/справочник.txt','r')
    last = data.readlines()[-1]
    data.close
    indexes = [i for (i,c) in enumerate(last) if c==';']
    if len(indexes)>0:
        processed_line.append(f';{str(int(last[indexes[-1]+1::])+1)}') 
        # находится последний символ ; и к значению 
        # после него прибавляется 1,затем снова преобразуется в строку
    else:
        processed_line.append(';1')
            
            
update = lambda x: x.clear()
    
def operation():
    return int(input('Выберите действие (1 - записать контакт в справочник),(0 - показать все данные справочника): '))


def create_file():
    with open('hw_lesson_7/справочник.txt','w') as data:
        data.write('Welcome to telephone directory!\n\n')






