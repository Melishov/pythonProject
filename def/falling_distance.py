def main():
    for t in range (1,11):
        distance=falling_distance(t)
        print(f"За {t} секунд(у), предмет пролетит {distance} метров")
def falling_distance(t):
    distance=1/(2*9.8*(t**2))
    return distance
main()