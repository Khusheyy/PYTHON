# heyy this is my first
#if the user gets the question right then inc by 1 point
print("welcome to my quiz")

playing = input("Do you want to play? : ")
#print(playing)

if playing.lower() != "yes":
    quit()
#quit the program if the user typed something other than "yes"
 
print("okayy lets playy :)")
score = 0

answer = input("what does the cpu stand for? ")
if answer.lower() == "central processing unit":
    print("coreectt!!")
    score +=1
else:
    print("incoreectt!!")
    
    
answer = input("what does the gpu stand for? ")
if answer.lower()  == "graphics processing unit":
    print("coreectt!!")
    score +=1
else:
    print("incoreectt!!")
    
    
answer = input("what does the llm stand for? ")
if answer.lower() == "large language model":
    print("coreectt!!")
    score +=1
else:
    print("incoreectt!!")
    
    
answer = input("what does the nlp stand for? ")
if answer.lower()  == "natural language processing":
    print("coreectt!!")
    score +=1
else:
    print("incoreectt!!")
    
print("You got " + str(score) + " questions correct! ")
print("You got " + str((score/4)*100) + " %.") 