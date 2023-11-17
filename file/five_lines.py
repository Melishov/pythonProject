def main():
    name_file=input("What is the file name?: \n")
    file_to_read=open(name_file,"r")
    for lines in range(5):
        line=file_to_read.readline()
        if line!="":
            line=line.rstrip("\n")
            print(line)
    file_to_read.close()
main()