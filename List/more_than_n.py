def main():
    list_of_numbers=[]
    answer='д'
    while answer=='д':
        list_of_numbers.append(int(input('Введите число для добавления в список: \n')))
        answer=input('Ещё одно число добавим? Если да, введите "д":\n')
    n=int(input('Введите число для сравнения с числами из предыдущего списка:\n'))
    print('Данные числа из списка больше чем число "n": \n')
    for number in list_of_numbers:
        if n<number:
            print(number)
main()