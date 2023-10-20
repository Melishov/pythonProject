MARK_UP=2.5
another="y"
while another=="y" or another=="Y":
    wholesale=float(input("Input cost of product: "))
    while wholesale<0:
        wholesale=float(input("Вы ввели отрицательное число, повторите попытку: "))
    print(f"Retail price of this product is: ${wholesale*MARK_UP:,.2f}")
    another=input("Another product, y/n? ")