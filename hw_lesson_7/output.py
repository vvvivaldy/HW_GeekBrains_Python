def out_file():
    data = open('hw_lesson_7/справочник.txt','r')
    for item in data:
        print(item, end='')
    print('\n')
    data.close()





