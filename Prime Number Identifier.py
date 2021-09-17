user_Input = int(input('Please type any number here'))

for i in range(2,user_Input//2):
    if user_Input % i == 0:
        print('Composite Number')
        break

else:
    print('Prime Number')

