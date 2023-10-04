import random
amount1=random.randint(0,20)
amount2=random.randint(0,200)
if amount1>10 and amount2<100:
    if amount1>amount2:
        print(amount1)
    else:
        print(amount2)
else:
    print("Условие не выполнено!")