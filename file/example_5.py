def main():
    read_file=open("data.txt","r")
    line=read_file.readline()
    while line!="":
        print(line)
        line = read_file.readline()
if __name__=="__main__":
    main()