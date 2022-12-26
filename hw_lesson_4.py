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






#5

def Open():
    with open('polynomial_1.txt(hw_4)','r') as data:
        poly1 = data.read()
    with open('polynomial_2.txt(hw_4)','r') as data:
        poly2 = data.read()
    return poly1, poly2
poly1, poly2 = Open()


def Create(poly):
     with open('polynomial_SUMM.txt(hw_4)','w') as data:
        data.write(poly)


def summ(poly1,poly2):
    poly1 = poly1.replace(' = 0','')
    poly1 = poly1.replace('x**', ' ')
    poly1 = poly1.replace(' + ',' ')
    poly1 = poly1.replace('x','1')
    poly1 = poly1.split()
    poly1 = list(map(int,poly1))

    poly2 = poly2.replace(' = 0','')
    poly2 = poly2.replace('x**', ' ')
    poly2 = poly2.replace(' + ',' ')
    poly2 = poly2.replace('x','1')
    poly2 = poly2.split()
    poly2 = list(map(int,poly2))

#из двух списков,где четные индексы - коэфиценты, нечетные - степени
#пытыюсь сложить коэфиценты двух списков опираясь на ключи
#надо каждый список рассматривать отдельно,чтобы сравнивать их степени

    if len(poly1)>len(poly2): 
        summ = [0] * len(poly1)
        for i in range(0,len(poly1)-2,2):
            if poly1[i+1]==poly2[i+1]:
                summ[-(i+1)] += poly1[i]+poly2[i]
            else:
                summ[-(i+1)] += poly1[i]
    else:
        summ = [0] * len(poly2)
        for i in range(0,len(poly2)-2,2):
            if poly1[i+1]==poly2[i+1]:
                summ[-(i+1)] += poly1[i]+poly2[i]
            else:
                summ[-(i+1)] += poly2[i]


    print(poly1)
    print(poly2)
    return summ
print(summ(poly1,poly2))



