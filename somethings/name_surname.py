PAYHOUR=int(input("Введите почасовую оплату труда:\n"))
PAYUP=1.5
hours=int(input("Сколько часов отработал сотрудник?\n"))
if hours<=40:
    print(f"Его зарплата составит {PAYHOUR*hours} рублей за этот месяц.")
else:
    print(f"Он работал сверхурочно, по-этому у него будут премиальные и его ЗП"
          f" составит {PAYHOUR*40+PAYUP*PAYHOUR*(hours-40)} рублей! Поздравляем!")

