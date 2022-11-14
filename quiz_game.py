print("Welcome To my Quiz!")
playing = input("Do you Want to play? (y/n) ")

if playing.lower() != "y":
    quit()

print("Okay! Lets play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!') 


answer = input("What is Best IDE? ")
if answer.lower() == "vs code":
    print('Correct!')
    score += 1
else:
    print('Incorrect! The correct answer is vs code') 

answer = input("What is best programing language? ").lower()
if answer == "python":
    print('Correct!')
    score += 1
else:
    print('Incorrect! its python') 
print(f"you got {score} questions correct!")
print(f"you got {(score/3)*100} %.")