def main():
    numbers=open("numbers.txt","w")
    for line in range(1,11):
        numbers.write(str(line)+"\n")
if __name__=="__main__":
    main()