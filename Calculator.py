print("Hello and welcome to the Simple Python Calculator!\n")

num1 = int(input("Give me a number.\n"))
num2 = int(input("Give me a second number.\n"))
operator = input("What operation do you want to do?\n")

if operator == "*":
    result = (num1 * num2)
elif operator == "/":
    result = (num1 / num2)
elif operator == "+":
    result = (num1 + num2)
elif operator == "-":
    result = (num1 - num2)
elif operator == "^":
    result = pow(num1, num2)
else:
    print("The operator you gave isn't correct.")
    exit(0)

print("The result is: " + str(result))