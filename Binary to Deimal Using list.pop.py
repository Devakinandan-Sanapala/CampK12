inp = list(input("Enter the binary number"))
var = 0

for i in range(len(inp)):
    if inp.pop() == "1":
        var+= 2**i
print(var)

