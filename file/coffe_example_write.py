def main():
    answer="д"
    list_coffe=open("coffe.txt","w")
    while answer=="д" or answer=="Д":
        sort=input("Введите название сорта кофе: \n")
        weight=float(input("Введите вес кофе: \n"))
        list_coffe.write(f"{sort}\n")
        list_coffe.write(f"{weight}\n")
        answer=input("Добавить ещё одну запись? д/н \n")
    list_coffe.close()
if __name__=="__main__":
    main()