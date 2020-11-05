print("Hello and welcome to the Simple Python Calculator!\n")

num1 = int(input("Give me a number.\n"))
num2 = int(input("Give me a second number.\n"))
opperator = input("What opperation do you want to do?\n")

if opperator == "*":
    result = (num1 * num2)
elif opperator == "/":
    result = (num1 / num2)
elif opperator == "+":
    result = (num1 + num2)
elif opperator == "-":
    result = (num1 - num2)
elif opperator == "^":
    result = pow(num1, num2)
else:
    print("The opperator you gave isn't correct.")
    exit(0)

print("The result is: " + str(result))