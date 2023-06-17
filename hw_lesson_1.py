
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




