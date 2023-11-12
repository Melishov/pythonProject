def main():
    file_list=open("number_list.txt","r")
    total=0
    num=file_list.readline()
    while num!="":
        num=num.rstrip("\n")
        num=int(num)
        total+=num
        print(f"число {num}, а сумма чисел равна {total}")
        num = file_list.readline()
    file_list.close()
if __name__=="__main__":
    main()
