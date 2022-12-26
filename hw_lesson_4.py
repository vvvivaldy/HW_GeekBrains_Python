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
    
