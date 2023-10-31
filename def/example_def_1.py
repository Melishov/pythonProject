def main():
    num1=int(input("Enter the first number: \n"))
    num2=int(input("Enter the second number: \n"))
    result_division=division(num1,num2)
    print(f"Result of division", num1, "and", num2, "is", result_division)
def division(num1,num2):
    if num2==0:
        result=0
    else:
        result=num1/num2
        return result
main()