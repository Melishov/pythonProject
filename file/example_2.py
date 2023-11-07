def main():
    read_from_num=open("num.txt","r")
    num=read_from_num.read()
    read_from_num.close()
    print(num)
if __name__=="__main__":
    main()