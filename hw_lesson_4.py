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
#             res.append('x')
        
#         elif (koef[i]!=0) and (i==0):
#             res.append(str(koef[i]))

#         elif (koef[i]==1) and i==1 or i==0:
#             res.append('1')

#     res.append(' = 0') 

#     result = ''.join(res) # превращяем список в строку

#     if result[0]==' ':
#         result = result.replace(' + ','',1) #удаляем лишний плюс если он есть

#     return result
    
# create(outpoly(k,rn(k)),outpoly(k,rn(k)))





# #5

# #считываем многочлены
# def Open():
#     with open('polynomial_1.txt(hw_4)','r') as data:
#         poly1 = data.read()
#     with open('polynomial_2.txt(hw_4)','r') as data:
#         poly2 = data.read()
#     return poly1, poly2


# # присваивыем считанные многочлены переменным
# poly1, poly2 = Open()


# # создаем файл для вывода 
# def Create(poly):
#      with open('polynomial_SUMM.txt(hw_4)','w') as data:
#         data.write(poly)


# # обрабатываем многочлен в вид списка,удаляя лишние символы
# def convert(poly):
#     poly = poly.replace(' = 0','')
#     poly = poly.replace('x**', ' ')
#     poly = poly.replace(' + ',' ')
#     poly = poly.replace('x','1')
#     poly = poly.split()
#     poly = list(map(int,poly))
#     if len(poly)%2==0:
#         temp = poly[-1]
#         poly[-1] = poly[-2]
#         poly[-2] = temp
#     return poly


# # конвертируем обработанный в список многочлен в словарь
# def convert_to_dict(poly):
#     dict1 = {}
#     if len(poly)%2==0:
#         for i in range(0,len(poly),2):
#             dict1[poly[i+1]] = poly[i]
#     else:
#         for i in range(0,len(poly),2):
#             dict1[poly[i+1]] = poly[i]

#     return dict1


# # сумма многочленов
# def summ (d1,d2): 
#     summa = []
#     if len(list(d1))>len(list(d2)): #проверка какой многочлен был больше(длиннее)
#         for (k,v) in d1.items():
#             for i in range(1,k+1):
#                 if (k==i) and (k!=1) and ((k in d2)==True):
#                     summa.append(v+d2[i])
#                 elif k==1 and i==1:
#                     summa.append(2)
#                     summa.append(d1[1]+d2[1])
#                 elif ((k in d2)==False):
#                     summa.append(v)
#                     break
#     else:
#         for (k,v) in d2.items():
#             for i in range(1,k+1):
#                 if (k==i) and (k!=1) and ((k in d1)==True):
#                     summa.append(v+d1[i])
#                 elif k==1 and i==1:
#                     summa.append(2)
#                     summa.append(d1[1]+d2[1])
#                 elif ((k in d1)==False):
#                     summa.append(v)
#                     break
#     return summa
    

# #собираем многочлен
# def outpoly(k):
#     result = ''
#     count = len(k)-1
#     for i in range(count): 
#         if count != 0 and count!=1:
#             k[i]= f'{str(k[i])}x**{count}'
#         elif count==1:
#             k[i]=f'{str(k[i])}x'
#         else:
#             k[i] = str(k[i])
#         count-=1
        
#     for i in range(len(k)):
#         if i != 0:
#             result+=f' + {k[i]}'
#         else:
#             result+=k[i]
#     result+=' = 0'
#     return result

# Create(outpoly(summ((convert_to_dict(convert(poly1))),(convert_to_dict(convert(poly2))))))




