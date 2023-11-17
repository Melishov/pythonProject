def main():
    name_file=input("What is the file name?: \n")
    file_to_read=open(name_file,"r")
    count=1
    line=file_to_read.readline()
    while line!="":
        line=line.rstrip("\n")
        print(count,": ",line, sep="")
        line = file_to_read.readline()
        count+=1
    file_to_read.close()
main()