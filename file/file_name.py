def main():
    file_for_name=open("my_name.txt",'w')
    name=input("Введите своё имя: \n")
    file_for_name.write(f"{name}\n")
    file_for_name.close()
    print("Ваше имя записано в файл my_name.txt")
if __name__=="__main__":
    main()