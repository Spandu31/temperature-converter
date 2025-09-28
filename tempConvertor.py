
print("Enter the temperature:")
num = float(input())

print("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius:")
unit = input()


print("You entered:", num, unit)

def calc(num, unit):
    if unit == "c" or unit == "C":
        temp = (num * 9/5) + 32
        print(f"Temperature in Fahrenheit:", f"{temp:.2f}", "F")
    elif unit == "f" or unit == "F":
        temp = (num - 32) * 5/9
        print("Temperature in Celsius:", f"{temp:.2f}", "C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
calc(num, unit)

