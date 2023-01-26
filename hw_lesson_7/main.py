from input import *
import controller as c
import output

op = c.operation()
c.create_file()
if op:
    while True:
        print('Чтобы выйти из режима записи, введите "выход"')
        fill()
        if processed_line[0] == 'выход':
            break
        else:
            c.add_id()
            c.open_file(c.to_str())
        c.update(processed_line)
else:
    output.out_file()
            
        

