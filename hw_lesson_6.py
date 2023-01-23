# #1
# xa = int(input("Введите координату X1: "))
# ya = int(input("Введите координату Y1: "))
# xb = int(input("Введите координату X2: "))
# yb = int(input("Введите координату Y2: "))

# A = (xa,ya)
# B = (xb,yb)

# vector = list(zip(A,B))
# stepen = lambda a: a**2
# koren = lambda a: a**0.5
# print(vector)
# print(koren(stepen(vector[0][1] - vector[0][0]) + stepen(vector[1][1] - vector[1][0])))

# #2
# list1 = ['1','2','3','4','5','6','7','8','9','10']
# list1 = list(map(int,list1))
# list2 = list(filter(lambda x: list1.index(x)%2,list1))
# print(sum(list2))

#3
# list1 = [i for i in range(1,11)]
# slovar = dict(enumerate(list1))
# mult = lambda a,b: a*b
# sum = 0
# key = list(slovar.keys())

# for i in range(len(list1)//2):
#     sum += mult(list1[min(key)],list1[max(key)])
#     del key[0]
#     del key[-1]

# if len(list1)%2:
#     sum+=list1[len(list1)//2]

# print(sum)



#4
# n = int(input())
# s =1
# f = lambda x: x*(-3)
# for i in range(0,n):
#     print(s,end = ' ')
#     s = f(s)



