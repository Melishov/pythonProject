import random
NUMBERS=9
COUNT_OF_NUM=7
numbers=[]
def main():
    for number in range(NUMBERS):
        numbers.append(number+1)
    num_list=[]
    #for count in range(COUNT_OF_NUM):
        #num_list.append(random.randint(0,9))
    num_list=random.sample(numbers,k=COUNT_OF_NUM)
    for element in num_list:
        print('|',element,'|',end="")
main()