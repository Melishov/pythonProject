import random
even_count=0
not_even_count=0
for count in range(1,101):
    num=random.randint(1,10000)
    if num%2==0:
        even_count+=1
    else:
        not_even_count+=1
print(f"Чётных чисел было: {even_count}, нечётных было: {not_even_count}")
