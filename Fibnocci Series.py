inp = int(input("Please enter the number of times you would like the series to repeat"))

first_Number = 0
second_Number = 1
third_Number = 0
print(0)
print(1)

for i in range(0,inp-2):
    third_Number = first_Number + second_Number
    print(third_Number)
    first_Number = second_Number
    second_Number = third_Number
        
    
    

    
