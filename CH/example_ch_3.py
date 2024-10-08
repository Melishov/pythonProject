mystring='Привет 123 кратный лох!11'
counter=0
for ch in mystring:
    if ch.isnumeric():
        counter+=1
print('Количество цифр в строке равно: '+ str(counter))