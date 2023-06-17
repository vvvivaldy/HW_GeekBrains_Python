def out_file():
    data = open('d:/1_GoGoCode/GoGoPython/HW_Python_GeekBrains/hw_lesson_7/справочник.txt','r')
    for item in data:
        print(item, end='')
    print('\n')
    data.close()





