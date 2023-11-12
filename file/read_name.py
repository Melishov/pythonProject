def main():
    name_file=open("my_name.txt","r")
    name=name_file.readline()
    name=name.rstrip("\n")
    print(name)
    name_file.close()
if __name__=="__main__":
    main()