
processed_line = []
def fill():
    global processed_line
    line = list(input(' Введите контакт в формате "Имя Фамилия номер_телефона комментарий".\n Комментарий пишется в одно слово, или вместо пробела используйте _.\n Ввод: ').split())
    for i in range(len(line)):
        if line[i]!=line[-1]:
            processed_line.append(f'{line[i]};')
        else:
            processed_line.append(line[i])
    


    
            
            