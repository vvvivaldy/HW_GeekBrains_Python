# #1
# list1 = list(map(int,input().split()))
# summ = 0
# for i in range(len(list1)-1):
#     if i%2!=0:
#         summ+=list1[i]
# print(summ)



#2
# list1 = list(map(int,input().split()))
# if len(list1)%2==0:
#     for i in range(len(list1)//2):
#         summ = int(list1[0])*int(list1[-1])
#         print(summ, end=' ')
#         del list1[0], list1[-1]
# else:
#     for i in range((len(list1)+1)//2):
#         if len(list1)>1:
#             summ = int(list1[0])*int(list1[-1])
#             print(summ, end=' ')
#             del list1[0], list1[-1]
#         elif len(list1)==1:
#             summ = list1[0]**2
#             print(summ)




# #3
# fl = list(map(float,input().split()))
# for i in range(len(fl)):
#     fl[i] = fl[i]-int(fl[i])
# print(max(fl)-min(fl))




#4
# n = int(input())
# print(bin(n).replace('0b',''))




#5

n = int(input())
lst = [fibonacci(i) for i in range(0, n+1)] # создаем список из чисел фибоначи
lst = lst[::-1] + lst[1:] # создается список из самого себя(сначала с последнего до первого эл)
                            # потом со второго(т.к. индексация с 0) по последний

for i in range(len(lst)): #добавляем в нужные места ' - '
    if i <=len(lst)//2+1 and i%2==0:
        lst[i]*=-1

print(lst, '\n')

def fibonacci(n): # ф-ция чисел фибоначи
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


