def main():
    count=1
    employ_file=open("employees.txt","r")
    name=employ_file.readline()
    while name!="":
        id=employ_file.readline()
        dept=employ_file.readline()
        name=name.rstrip("\n")
        id=id.rstrip("\n")
        dept=dept.rstrip("\n")
        print(f"Сотрудник №{count}:")
        print(f"Имя: {name}")
        print(f"id: {id}")
        print(f"Отдел: {dept}")
        print()
        name = employ_file.readline()
        count+=1
if __name__=="__main__":
    main()
