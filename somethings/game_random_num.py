import random
while True:
    num=random.randint(1,20)
    count=1
    print('Я загадал число от 1 до 20, попробуй его угадать: ')
    while True:
        user_num=int(input())
        if user_num==num:
            print('Ты угадал с ' + str(count) + ' попытки, молодец!')
            break
        elif user_num<num:
            count+=1
            print("Твоё число меньше, чем я загадал, попробуй ещё раз!")
        else:
            count+=1
            print("Твоё число больше моего, попробуй ещё раз!")
    answer=input("Будешь еще раз пробовать? да/нет ")
    if answer=='да':
        continue
    else:
        break
print("Пока!")