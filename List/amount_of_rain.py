def main():
    amount_of_rain=[]
    months=[x for x in range(1,13)]
    summary=0
    for month in months:
        amount=(int(input(f"Input amount of rain for the {month} month:\n")))
        amount_of_rain.append(amount)
        summary+=amount
    average_value=summary/12
    max_amount=max(amount_of_rain)
    min_amount=min(amount_of_rain)
    max_month=amount_of_rain.index(max_amount)+1
    min_month=amount_of_rain.index(min_amount)+1
    print(f"For this year it was {summary} rain, in average it was {average_value} rain, max rain was in {max_month} month, min rain was in {min_month} month")
main()


