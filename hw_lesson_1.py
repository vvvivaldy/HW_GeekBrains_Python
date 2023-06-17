#1
# day = int(input("Введите день недели: "))
# print(day==6 or day==7)


#2
# print ("x y z -> result")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f"{x} {y} {z} -> ", not(x+y+z>0)==(not(x) and not(y) and not(z)))

#3
# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))

# if x>0 and y>0:
#     print(1)
# elif x<0 and y>0:
#     print(2)
# elif x<0 and y<0:
#     print(3)
# elif x>0 and y<0:
#     print(4)
# elif x==0 and y!=0:
#     print("На оси X")
# elif y==0 and x!=0:
#     print("На оси Y")
# else:
#     print("В начале координат")

#4
# y = int(input("Enter: "))
# if y==1:
#     print('x(0;+бесконечость) y(0;+бесконечость)')
# elif y==2:
#     print('x(0;-бесконечость) y(0;+бесконечость)')
# elif y==3:
#     print('x(0;-бесконечость) y(0;-бесконечость)')
# elif y==4:
#     print('x(0;+бесконечость) y(0;-бесконечость)')

#5
import math
xa = int(input('Enter Xa: '))
ya = int(input('Enter Ya: '))
xb = int(input('Enter Xb: '))
yb = int(input('Enter Yb: '))

print(f'A({xa};{ya}), B({xb};{yb}) -> {round(math.sqrt((xb-xa)**2+(yb-ya)**2),2)}')




