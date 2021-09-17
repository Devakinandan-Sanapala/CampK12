import random

user_Input = input("Please choose rock paper or scissors")
lis = ["rock","paper","scissors"]

computer = random.choice(lis)

if computer == user_Input:
    print("The game is a tie")

else:
    if user_Input == "rock" and computer == "scissors":
        print("Rock breaks Scissor User has won")

    elif computer == "rock" and user_Input == "scissors":
        print("Rock breaks Scissor Computer has won")

    elif user_Input == "rock" and computer == "paper":
        print("Rock is surrounded by Paper Computer has won")

    elif computer == "rock" and user_Input == "paper":
        print("Rock is surrounded by Paper User has won")


    elif user_Input == "paper" and computer == "rock":
        print("Rock is surrounded by Paper User has won")

    elif computer == "paper" and user_Input == "rock":
        print("Rock is surrounded by Paper Computer has won")

    elif user_Input == "paper" and computer == "scissors":
        print("Paper has cut been by Scissor Computer has won")

    elif computer == "paper" and user_Input == "scissors":
        print("Paper has been cut by Scissor User has won")


    elif user_Input == "scissors" and computer == "paper":
        print("Paper has been cut by Scissor User has won")

    elif computer == "scissors" and user_Input == "paper":
        print("Paper has been cut by Scissor Computer has won")

    elif user_Input == "scissors" and computer == "rock":
        print("Scissor has been broken by Rock Computer has won")

    elif computer == "scissors" and user_Input == "rock":
        print("Scissor has been broken by Rock User has won")

    elif user_Input != "rock" or "scissors" or "paper":
        print("Please enter a valid input or check your spelling")



    


    

    