#1 
# import math
# d = input()
# print(round(math.pi,len(d)-2))



#2
# n = int(input())
# list1 = []
# while n!=0:
#     for i in range(2,n+1):
#         if n%i==0:
#             list1.append(i)
#             break
#     n//=list1[-1]
# print(list1)




#3
# n = list(map(int,input('Введите элементы списка: ').split()))
# n2 = set(n)
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]==n[j]:
#             n2.discard(n[i])
# print('Вот список без повторяющихся элементов: ',list(n2))
    



#4
# import random


# k = int(input("Введите степень: "))


# def create(poly,poly2): #Создадим не 1, а два файла с многочленами для решения следующей задачи
#     with open('polynomial_1.txt(hw_4)','w') as data:
#         data.write(poly)
#     with open('polynomial_2.txt(hw_4)','w') as data:
#         data.write(poly2)

# def rn(n): #создаем рандомные коэффиценты
#     koef = [random.randint(0,100) for i in range(n+1)]
#     return koef

# def outpoly(k,koef): # создаем многочлены
#     res = []
#     for i in range(k,-1,-1):

#         if (i<k) and (koef[i]!=0):
#             res.append(' + ')

#         if koef[i]==0:
#             res.append('')

#         elif (koef[i]==1) and (i!=1) and (i!=0):
#             res.append(f'x**{i}')

#         elif (koef[i]!=0) and (i!=1) and (i!=0):
#             res.append(f'{str(koef[i])}x**{str(i)}')
        
#         elif (koef[i]!=0) and (i==1):
#             res.append(f'{koef[i]}x')
        
#         elif (koef[i]!=0) and (i==0):
#             res.append(str(koef[i]))

#         elif (koef[i]==1) and i==1 or i==0:
#             res.append('1')

#     res.append(' = 0') 

#     result = ''.join(res) # превращяем список в строку

#     if result[0]==' ':
#         result = result.replace(' + ','',1) #удаляем лишний плюс если он есть
#     res = list(result)
#     res.insert(0,' ')
#     result = ''.join(res)
#     return result
    
# create(outpoly(k,rn(k)),outpoly(k,rn(k)))





#5


#считываем многочлены DONE
def Open():
    with open('polynomial_1.txt(hw_4)','r') as data:
        poly1 = data.read()
    with open('polynomial_2.txt(hw_4)','r') as data:
        poly2 = data.read()
    return poly1, poly2


# присваивыем считанные многочлены переменным DONE
poly1, poly2 = Open()


# создаем файл для вывода DONE
def Create(poly):
     with open('polynomial_SUMM.txt(hw_4)','w') as data:
        data.write(poly)


# обрабатываем многочлен в вид списка,удаляя лишние символы DONE
def convert(poly):
    poly = poly.replace(' x',' &$').replace('**','-').replace('x-',' ').replace('-',' ').replace('$','x')
    poly = poly.replace(' = 0','')
    poly = poly.replace(' + ',' ')
    a = poly.find('&x')
    if int(poly[1]) in range(1,10):
        poly = poly[1:]
    
    if ( poly[-1].isdigit() ) and (a>=0) and (len(list(poly.split()))%2!= 0):
        poly = poly.replace('&x',' 1')    
        poly = poly.replace('x',' 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)
        print(poly)

    elif ( len(list(poly.split()))%2== 0 ) and (a>=0) and ( poly[-1].isdigit() ):
        poly = poly.replace('&x','1 1') 
        poly = poly.replace('x',' 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)

    elif (len(list(poly.split()))%2== 0) and (a==-1) and ( poly[-1].isdigit()==False ):
        poly = poly.replace('x','1 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)
        poly.append(0)

    elif ( poly[-1].isdigit() == False ) and (a>=0) and (len(list(poly.split()))%2== 0):
        poly = poly.replace('&x',' 1')    
        poly = poly.replace('x',' 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)
        poly.append(0)
    
    elif ( poly[-1].isdigit() == False ) and (a>=0) and (len(list(poly.split()))%2!= 0):
        poly = poly.replace('&x','1 1')    
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)
        poly.append(0)
    
    elif ( poly[-1].isdigit() ) and (a==-1) and (len(list(poly.split()))%2== 0):
        poly = poly.replace('&x','1 1')    
        poly = poly.replace('x',' 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)

    elif (len(list(poly.split()))%2!= 0) and (a==-1) and ( poly[-1].isdigit()==False ):
        poly = poly.replace('x',' 1')
        poly = poly.split()
        poly = list(map(int,poly))
        poly.append(0)
        poly.append(0)

    return poly

# конвертируем обработанный в список многочлен в словарь DONE
def convert_to_dict(poly):
    dict1 = {}
    if len(poly)%2==0:
        for i in range(0,len(poly),2):
            dict1[poly[i+1]] = poly[i]
    return dict1

# сумма многочленов
def summ (d1,d2): 
    summa = []
    koef = []
    if len(list(d1))>len(list(d2)): #проверка какой многочлен больше(длиннее)
        for (k,v) in d1.items():
            koef.append(k)
            for i in range(0,k+1):
                if (k==i) and (k!=0) and (k in d2):
                    summa.append(v+d2[i])
                elif k==0 and i==0:
                    summa.append(d1[0]+d2[0])
                elif ((k in d2)==False):
                    summa.append(v)
                    break
    else:
        for (k,v) in d2.items():
            koef.append(k)
            for i in range(0,k+1):
                if (k==i) and (k!=0) and (k in d1):
                    summa.append(v+d1[i])
                elif k==0 and i==0:
                    summa.append(d1[0]+d2[0])
                elif ((k in d1)==False):
                    summa.append(v)
                    break
    return summa, koef

#собираем многочлен
def outpoly(k,koef):
    result = ''
    count = len(k)
    if k[-1] == 0:
        del k[-1]

    for j in range(len(koef)-1):
        if koef[j] > 1:
            k[j] = f'{str(k[j])}x**{koef[j]}'
        if koef[j] == 1:
            k[j] = f'{str(k[j])}x'
        if koef[j] == 0:
            k[j] = f'{str(k[j])}'

        
    for i in range(len(k)):
        if i != 0:
            result+=f' + {k[i]}'
        else:
            result+=str(k[i])
    result+=' = 0'
    return result


summa, koef = summ(convert_to_dict(convert(poly1)),convert_to_dict(convert(poly2)))
result = outpoly(summa,koef)
Create(result)




