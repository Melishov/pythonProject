def main():
    file_for_count=open("names.txt","r")
    counter=0
    line=file_for_count.readline()
    while line!="":
        counter+=1
        line = file_for_count.readline()
    file_for_count.close()
    print(f"File have {counter} lines")
main()