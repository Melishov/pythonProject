while True:
    length1=float(input("Введите длинну первого прямоугольника: \n"))
    width1=float(input("Введите ширину первого прямоугольника: \n"))
    length2=float(input("Введите длинну второго прямоугольника: \n"))
    width2=float(input("Введите ширину второго прямоугольника: \n"))
    square1=length1*width1
    square2=length2*width2
    if square1>square2:
        print("Площадь первого прямоугольника больше площади второго!")
    elif square1==square2:
        print("Площади прямоугольников равны!")
    else:
        print("Площадь первого прямоугольника меньше площади второго!")