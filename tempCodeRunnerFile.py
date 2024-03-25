def what_temperature():
    while True:
        try:
            fahrenheit = float(input("Please enter the temperature in Fahrenheit"))
            celsius = (fahrenheit - 32)* 5 / 9
            print(f"The temperature in celsius is: {celsius}")
            break
        except ValueError:
            print("Not a valid input, please try again using a number")
print("Thank you for trying out my app!!")
what_temperature()
