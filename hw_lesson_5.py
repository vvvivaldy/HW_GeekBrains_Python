
#1
#line = input()
#x = line.replace('абв','')
#print (x)

#2
#place = [['*','*','*'],['*','*','*'],['*','*','*']]
#def pr():
#    for i in range(3):
#        print(*place[i])
#pr()

#def move(x,sim):
#    if x<4 and place[0][x-1]=='*':
#        place[0][x-1] = sim
#    elif x>3 and x<7 and place[1][x-4]=='*':
#        place[1][x-4] = sim
#    elif x>6 and x<10 and place[2][x-7]=='*':
#        place[2][x-7] = sim
#    else:
#        print('Эта позиция уже занята! Попробуйте снова')
#        global symbol
#        symbol = change(symbol)
#        global t
#        t-=1

#gor = lambda line,i: line[i][0] == line[i][1] and line[i][0]!='*' and line[i][1] == line[i][2]

#vert = lambda line,j: line[0][j] == line[1][j] and line[0][j]!='*' and line[0][j] == line[2][j]

#diag = lambda line: (line[0][0] == line[1][1] and line[0][0]!='*' and line[0][0] == line[2][2]) or (line[0][2] == line[1][1] and line[0][2]!='*' and line[0][2] == line[2][0])

#symbol = 'x'
#def change(sym):
#    if sym=='x':
#        sym = 'o'
#    else:
#        sym = 'x'
#    return sym
#t=0
#while t<9:
#    move(int(input(f'Введите позицию {symbol}: ')),symbol)
#    if diag(place):
#        pr()
#        print('Победа {} !'.format(symbol))
#        break
#    for i in range(3):
#        for j in range(3):
#            if gor(place,i) or vert(place,j):
#                pr()
#                print('Победа {} !'.format(symbol))
#                t=9
#                break
             
#    if t==8:
#        print('Ничья!')
#        break
#    pr()
#    symbol = change(symbol)
#    t+=1


#3
line = input('Введите данный для сжатия/разжатия: ')

def compress(x):
    count=1
    output = ''
    tmp=x[0]
    while x!='':
        count=1
        tmp=x[0]
        for i in x[1::]:
            if tmp==i:
                count+=1
            else:
                break
        output += f'{count}{tmp}'
        x = x.replace(str(count*tmp),'',1)
    return output

def recovery(x):
    output=''
    helper = []
    for i in x:
        if i.isdigit():
            output+=i
        else:
            helper.append(int(output))
            output = ''
    output=''
    while x!='':
        x = x.replace(str(helper[0]),'',1)
        output += helper[0]*x[0]
        x = x[1::]
        helper.pop(0)
    return output

if int(input('Что вы хотите сделать? (0 - разжать; 1 - сжать): ')):
    print(compress(line))
else:
    print(recovery(line))
        






