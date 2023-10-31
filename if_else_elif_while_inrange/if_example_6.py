import random
speed=random.randint(0,100)
if(speed>24 and speed<56):
    print("Скорость нормальная:",speed)
else:
    print("Скорость аварийная:",speed)