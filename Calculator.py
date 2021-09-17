while exi != "N":
    fnum = int(input("Please enter your first number: "))
    snum = int(input("Please enter your second number: "))
    operator = input("Please enter your operator: ")

    if operator == "+":
        print(fnum + snum)

    elif operator == "-":
        print(fnum - snum)

    elif operator == "*":
        print(fnum * snum)

    elif operator == "/":
        print(fnum // snum)

    else:
        print("Please type a valid operator")

    exi = input("Do you want to continue? Y/N")