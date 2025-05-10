import random

#print(random.randrange(-1,11))
# takes any number below 10 , num < 10
# here 10 is the absolute upper bound

top_range = input("type a number : ")

if top_range.isdigit:
    top_range = int(top_range)
    
    if top_range == 0:
        print("please type a number greater than 0.")
        quit()
        
else:
    print("please enter a NUMBER next time. ")
    quit()
    
    
random_number = random.randint(0 , top_range)
guess = 0

while True:
    guess += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("please enter a number next time. ")
        continue
       # rather than ending the loop , it brings back the flow to top
     
    if user_guess == random_number:
        print("You got it right!")
        break
    
    else:
        #print("You got it WRONG , better luck next time")
        if user_guess > random_number :
            print("you were above the number!")
        else:
            print("you were below the number")
            
        
      
print("You got it in ", guess ,"guesses ")   