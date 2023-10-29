def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Unit Converter:")
    print("Choose the type of conversion:")
    print("1. Temperature Converter (Celsius to Fahrenheit and vice versa)")
    print("2. Length Converter (Meters to Feet and vice versa)")
    print("3. Weight Converter (Kilograms to Pounds and vice versa)")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        try:
            value = float(input("Enter the temperature value: "))
            print("Choose conversion direction:")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            direction = input("Enter your choice (1/2): ")
            
            if direction == '1':
                result = celsius_to_fahrenheit(value)
                print(f"{value}°C is equal to {result}°F")
            elif direction == '2':
                result = fahrenheit_to_celsius(value)
                print(f"{value}°F is equal to {result}°C")
            else:
                print("Invalid choice for conversion direction. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    elif choice == '2':
        try:
            value = float(input("Enter the length value: "))
            print("Choose conversion direction:")
            print("1. Meters to Feet")
            print("2. Feet to Meters")
            direction = input("Enter your choice (1/2): ")
            
            if direction == '1':
                result = meters_to_feet(value)
                print(f"{value} meters is equal to {result} feet")
            elif direction == '2':
                result = feet_to_meters(value)
                print(f"{value} feet is equal to {result} meters")
            else:
                print("Invalid choice for conversion direction. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    elif choice == '3':
        try:
            value = float(input("Enter the weight value: "))
            print("Choose conversion direction:")
            print("1. Kilograms to Pounds")
            print("2. Pounds to Kilograms")
            direction = input("Enter your choice (1/2): ")
            
            if direction == '1':
                result = kilograms_to_pounds(value)
                print(f"{value} kilograms is equal to {result} pounds")
            elif direction == '2':
                result = pounds_to_kilograms(value)
                print(f"{value} pounds is equal to {result} kilograms")
            else:
                print("Invalid choice for conversion direction. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
