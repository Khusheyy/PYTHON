import random

user_wins = 0
computer_wins = 0

options = ["rock" , "paper" , "scissors"]
# list for options

while True:
    user_input = input("type rock / paper / scissor OR Q to quit the game : ").lower()
    
    if user_input == 'q':
        break
    
    if user_input not in["rock" , "paper" , "scissor"]:
        print("the text entered is not valid")
        continue
    
    random_number = random.randint(0,2)
    # rock : 0
    # paper : 1
    # scissor : 2
    
    computer_pick = options[random_number]
    print("the computer picked," , computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You WON!!")
        user_wins += 1
        
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You WON!!")
        user_wins += 1
        
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("You WON!!")
        user_wins += 1
       
    else:
        print("You lost!")
        computer_wins += 1
        
print("you won ",user_wins," times..")
print("computer won",computer_wins,"times .")
 
    
print("gooddbyee")