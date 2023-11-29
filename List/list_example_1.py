NUM_DAYS=5
def main():
    sales=[0]*NUM_DAYS
    for day in range(NUM_DAYS):
        sales[day]=float(input(f"Input sales for {day+1} day: "))
    for meaning in sales:
        print(f"Meaning: {meaning}")
if __name__=="__main__":
    main()