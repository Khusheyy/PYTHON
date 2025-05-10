# children's book adventure type , based on decision making
# do you wanna climb this bridge : yes/no , if yess here you goo swimming....
 
name = input("Type your name : ")
print("Welcome ",name," to this game!!")

answer = input("You are on a diet road , it has come to an end and you can only go left or right . which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river and if you can walk around it or swim across. Type walk to walk around OR swim to swim across ")
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator! ")
    elif answer == "walk":
        print("You walked for many miles , ran out of water and lost the game ")
    else:
        print("Not a valid option. you lose :( ")
        
elif answer =="right":
    answer = input("You come to a bridge , it looks wobbly . do you wanna crsoo it or head back (cross/back)? ")
    
    if answer == "cross":
        #print(" ohhh nooo the bridge broke off , you fell and die!!")
        
        answer = input("you cross the bridge , and see a stranger . Do you talk to them? (yes/no) ")
        
        if answer == "yes":
             print("the stranger turns out to be your old school friend!! , lfgg ")
        elif answer == "no":
             print("ignore the stranger and they get offended! :( ")
        else:
            print("not a valid option. you lose :( ") 
             
    elif answer == "back":
        print("thankgodd the bridge brokee off and you saved your life by not risking that one step")
    else:
        print("not a valid option. you lose :( ")
else:
    print("not a valid option. you lose :( ")