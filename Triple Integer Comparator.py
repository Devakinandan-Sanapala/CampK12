one = int(input("Please type the first number"))
two = int(input("Please type the second number"))
three = int(input("Please type the third number"))

if (one > two) and (one > three):
    print("One is the largest number")

elif (two > one) and (two > three):
    print("Two is the largest number")

elif one == two == three:
    print("All numbers are equal")

else:
    print("Three is the largest number")