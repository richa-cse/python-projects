print("Welcome to python quiz game")
score=0
answer1=input("1.what is the capital of india?")
if answer1.lower()=="delhi":
    print("correct!")
    score+=1
else:
    print("wrong!")
answer2=input("2.which languare are we learning?")
if answer2.lower()=="python":
    score+=1
else:
    print("wrong!")
answer3=input("3.5+5=")
if answer3=="10":
    print("correct!")
    score+=1
else:
    print("wrong!")
print("your final score is:",score)    