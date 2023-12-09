def main():
    day_of_week=['monday','tyesday', 'wednesday','thursday','friday','saturday','sunday']
    earnings=[]
    summary=0
    try:
        for day in day_of_week:
            day_earnings=(int(input("What earnings was in " + day + "?\n")))
            earnings.append(day_earnings)
            summary+=day_earnings
    except ValueError as ve:
        print("Enter only numbers!")
    except IOError as io:
        print("Enter only numbers!")
    else:
        print(f"Total earnings for week is ${summary:.2f}")
main()