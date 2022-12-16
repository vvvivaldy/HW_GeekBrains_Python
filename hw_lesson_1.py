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
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)
elif x==0 and y!=0:
    print("На оси X")
elif y==0 and x!=0:
    print("На оси Y")
else:
    print("В начале координат")
