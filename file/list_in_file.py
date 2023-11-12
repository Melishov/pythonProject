def main():
    list_file=open("number_list.txt","w")
    for number in range (1,101):
        number=str(number)
        list_file.write(f"{number}\n")
    list_file.close()
if __name__=="__main__":
    main()
