pocket=int(input("Введите число от нуля до 36, чтобы я Вам сообщил цвет колеса рулетки данной ячейки!: \n"))
if 1<=pocket<=10:
    if pocket%2==0:
        print("Цвет ячейки-чёрный")
    else:
        print("Цвет ячейки-красный")
elif 11<=pocket<=18:
    if pocket%2==0:
        print("Цвет ячейки-красный")
    else:
        print("Цвет ячейки-чёрный")
elif 19<=pocket<=28:
    if pocket%2==0:
        print("Цвет ячейки-чёрный")
    else:
        print("Цвет ячейки-красный")
elif 29<=pocket<=36:
    if pocket%2==0:
        print("Цвет ячейки-красный")
    else:
        print("Цвет ячейки-чёрный")
elif pocket==0:
    print("Цвет ячейки-зелёный")
else:
    print("Вы ввели число вне диапазона!")
