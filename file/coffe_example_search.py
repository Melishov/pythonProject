def main():
    search=False
    key_word=input("Введите точное название для поиска: \n")
    coffe=open("coffe.txt", "r")
    name=coffe.readline()
    while name!="":
        quantity=float(coffe.readline())
        name=name.rstrip("\n")
        if key_word==name:
            print(f"Описание: {name}")
            print(f"Количество: {quantity}")
            print()
            search=True
        name = coffe.readline()
    if not search:
        print("Значение не найдено! Проверьте правильность написания!")
    coffe.close()
if __name__=="__main__":
    main()
