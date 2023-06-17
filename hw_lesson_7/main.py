from input import *
import controller as c
import output
import os

op = c.operation()
if os.path.isfile('d:/1_GoGoCode/GoGoPython/HW_Python_GeekBrains/hw_lesson_7/справочник.txt') == False:
    c.create_file()
if op:
    while True:
        print('Чтобы выйти из режима записи, введите "exit"')
        fill()
        if processed_line[0] == 'exit':
            break
        else:
            c.add_id()
            c.open_file(c.to_str())
        c.update(processed_line)
else:
    output.out_file()
            
        

