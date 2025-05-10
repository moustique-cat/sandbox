def meters_to_kilometers(meters):
    return meters / 1000

def main():
    print("Welcome to the Unit Converter!")
    
    meters = float(input("Enter distance in meters: "))
    kilometers = meters_to_kilometers(meters)
    print(f"{meters} meters is {kilometers} kilometers.")

if __name__ == "__main__":
    main()