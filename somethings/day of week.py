min_value = 1  # Минимальное значение
max_value = 7
while True:
    try:
        number = int(input(f"Введите число между {min_value} и {max_value}: \n"))
        if min_value <= number <= max_value:
            break  # Выход из цикла, если число в диапазоне
        else:
            print(f"Число должно быть между {min_value} и {max_value}. Попробуйте еще раз.")
    except ValueError:
        print(f"Пожалуйста, введите целое число в диапазоне от {min_value} до {max_value}!")

if number==1:
    week='Понедельник'
elif number==2:
    week="Вторник"
elif number==3:
    week="Среда"
elif number==4:
    week="Четверг"
elif number==5:
    week="Пятница"
elif number==6:
    week="Суббота"
else:
    week="Воскресенье"
print(f"Введённому Вами числу соответствует денье недели: {week}!")