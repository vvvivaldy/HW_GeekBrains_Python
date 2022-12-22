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
#3


#4
# n = int(input())
# print(bin(n).replace('0b',''))

#5