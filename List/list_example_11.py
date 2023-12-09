def main():
    list=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    k=0
    el=0
    for element in list:
        subel=0
        for subelement in element:
            list[el][subel]=(int(input(f"Input value for {k+1} element in list:\n")))
            k+=1
            subel+=1
        el+=1
    print(list)
main()