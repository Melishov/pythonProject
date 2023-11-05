answer="y"
while answer=="y" or answer=='Y':
    num_1=int(input("Введите первое число: "))
    num_2=int(input("Введите второе число: "))
    print(f"Сумма этих чисел равна: {num_1+num_2}")
    answer=input("Повторить рассчёт? y/n: ")