inp = input("Enter numbers").split(",")
max = inp[0]

for i in range(0,len(inp)):
    if int(max) < int(inp[i]):
        max,inp[i] = inp[i],max

print(max)
