def list_summ(list_for_summ):
    k=0
    for element in list_for_summ:
        k+=element
    return k
def main():
    list=[99,88,77,45,890,87,67,67,86,86]*100
    summ=list_summ(list)
    print(summ)
main()