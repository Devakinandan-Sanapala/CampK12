Numbers = [1,2,5,7,8,89,9,7,54,3,0,91,93,57,62,66]
user_Input = int(input("Enter any number here"))

# for i in range(0,len(Numbers)):
#     if user_Input == Numbers[i]:
#         print("Number Found")
#         break

# else:
#     print("Number Not Found")

for item in Numbers:
    if user_Input == item:
        print("Number Found")
        break

else:
    print("Number Not Found")