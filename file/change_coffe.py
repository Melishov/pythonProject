import os
def main():
    found=False
    search=input("Введите название позиции, количество которой хотим изменить: \n")
    new_qty=float(input("Укажите новое количество: \n"))
    file_coffe=open("coffe.txt","r")
    new_file_coffe=open("tmp.txt","w")
    name=file_coffe.readline()
    while name!="":
        name=name.rstrip("\n")
        qty=float(file_coffe.readline())
        if search==name:
            new_file_coffe.write(f"{name}\n")
            new_file_coffe.write(f"{new_qty}\n")
            found=True
        else:
            new_file_coffe.write(f"{name}\n")
            new_file_coffe.write(f"{qty}\n")
        name=file_coffe.readline()
    file_coffe.close()
    new_file_coffe.close()
    os.remove("coffe.txt")
    os.rename("tmp.txt","coffe.txt")
    if found:
        print("Фаил обновлён новыми данными")
    else:
        print("Запись не найдена!")
if __name__=="__main__":
    main()
