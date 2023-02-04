candy = 221
test_move = [i for i in range(29,221,28)]
a = 0
print(test_move)
while candy > 0:
    move_person = int(input("я: "))
    candy -=move_person
    if a==0:
        if move_person<24:
            move = 24-move_person
            a=1
        else:
            move = 24
            a=1
    elif candy<=28:
            move=candy
    elif move_person != 28 and move_person!= None:
        move = 28-move_person
    elif move_person!=None:
        move = candy

    candy -=move
    print(move, candy)
