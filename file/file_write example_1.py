def main():
    emp_count=int(input("Сколько сотрудников вы хотите занести в фаил в виде данных о них?\n"))
    emp_file=open("employees.txt","w")
    for employ in range(1, emp_count+1):
        name=input(f"Введите имя сотрудника №{employ}: \n")
        id=input(f"Введите уникальный номер сотрудника №{employ}: \n")
        dept=input(f"Введите отдел, где работает сотрудник №{employ}: \n")
        emp_file.write(name + "\n")
        emp_file.write(id + "\n")
        emp_file.write(dept + "\n")
        print()
    emp_file.close()
if __name__=="__main__":
    main()