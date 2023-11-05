def main():
    km=int(input("Enter kilometers to convert in miles: \n"))
    miles=convert_km_to_miles(km)
    print(f"Distance in miles is: {miles:.2f}")
def convert_km_to_miles(km):
    miles=km*0.6214
    return miles
main()