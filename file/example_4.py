def main():
    read_file=open("data.txt","r")
    for line in read_file:
        line.rstrip("\n")
        print(line)
if __name__=="__main__":
    main()