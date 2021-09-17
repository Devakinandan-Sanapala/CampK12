inp = input("Enter numbers").split(",")
min = inp[0]

for i in range(0,len(inp)):
    if int(min) > int(inp[i]):
        min,inp[i] = inp[i],min

print(min)