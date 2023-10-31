import random
score=random.randint(0,100)
if score>=90:
    print('Your score is "A"! ')
else:
    if score>=80:
        print('Your score is "B"! ')
    else:
        if score>=70:
            print('Your score is "C"! ')
        else:
            if score>=60:
                print('Your score is "D"! ')
            else:
                print('Your score is "F"! ')