answer="y"
while answer=='y':
    sales=float(input("Введите сумму продаж:\n"))
    percent=float(input("Введите процент продавца: \n"))
    pay=sales*percent/100
    print(f"Доля продавца составит: ${pay:,.2f}")
    answer=input("Посчитать следующего продавца?\n Для ответа введите y/n: ")