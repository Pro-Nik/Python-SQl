import random
print("Game Started:")
print("Choose any one:")
i=0
j=0
while True:
    c =int(input('''
              1 Rock
              2 Paper
              3 Scissors
              4 Exit
            
            '''))
    if c==1:
        n = "Rock"
    if c==2:
        n = "Paper"
    if c==3:
        n= "Scissors"
    if c==4:
        break;
    print("You: " ,n)
    l = ["Rock","Paper","Scissors"]

    m = random.choice(l)
    print("Computer: ", m)

    if n =="Rock" and m =="Rock":
        print("Match Draw")
        continue
    if n =="Paper" and m =="Paper":
        print("Match Draw")
        continue
    if n =="Scissors" and m =="Scissors":
        print("Match Draw")
        continue

    if n =="Rock" and m =="Paper":
        print("Computer Wins")
        j=j+1
        continue
        
    if n =="Paper" and m =="Rock":
        print("You Wins")
        i=i+1
        continue
    if n =="Scissors" and m =="Paper":
        print("You Wins")
        i=i+1
        continue
    if n =="Paper" and m =="Scissors":
        print("Computer Wins")
        j=j+1
        continue
    if n =="Rock" and m =="Scissors":
        print("You Wins")
        i=i+1
        continue
    if n =="Scissors" and m =="Rock":
        print("Computer Wins")
        j=j+1
        continue

if i==j:
    print("Match Draw")
if i>j:
    print("You Wins")
if i<j:
    print("Computer Wins")