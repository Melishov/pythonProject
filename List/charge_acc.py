import os
def main():
    list_from_file=[]
    file=open("charge_accounts.txt","r")
    line=file.readline()
    while line!="":
        num_line=line.rstrip("\n")
        num_line=int(num_line)
        list_from_file.append(num_line)
        line = file.readline()
    file.close()
    number_of_user=int(input('Введите свой номер: \n'))
    if number_of_user in list_from_file:
        print("Такой номер есть, доступ разрешён!")
    else:
        print("Нет такого номера, иди в жопу!")
if __name__=="__main__":
    main()

