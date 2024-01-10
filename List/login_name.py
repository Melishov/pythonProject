import login
def main():
    name=input("Введите ваше имя:\n")
    last_name=input("Введите вашу фамилию: \n")
    id_number=input('Введите ваш айди номер: \n')
    login_name=login.get_login_name(name,last_name,id_number)
    print(f"Ваш логин в системе будет: {login_name}")
if __name__=="__main__":
    main()